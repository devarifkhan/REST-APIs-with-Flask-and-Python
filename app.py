import uuid
from flask import Flask
from db import items, stores
from flask import abort

app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/stote")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Name of the store is required")

    for store in store.values():
        if store["name"] == store_data["name"]:
            abort(
                400,
                message="A store with name {} already exists".format(
                    store_data["name"]
                ),
            )

    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201


@app.post("/item")
def create_item(name):
    item_data = request.get_json()
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(
            400,
            message="Bad request.Ensure price, store_id and name are included in the request",
        )

    if item_data["store_id"] not in stores:
        abort(404, message="store not found")

    for item in item.values():
        if (
            item_date["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(
                400,
                message="An item with name {} already exists in store {}".format(
                    item_data["name"], item_data["store_id"]
                ),
            )

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item
    return item, 201


@app.get("/item")
def all_get_items():
    return {"items": list(items.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="store not found")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="item not found")


@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "item deleted"}
    except KeyError:
        abort(404, message="item not found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    item_data = request.get_json()
    if "price" not in item_data or "name" not in item_data:
        abort(
            400,
            message="Bad request.Ensure price and name are included in the request",
        )
    try:
        item = items[item_id]
        item |= item_data
    except KeyError:
        abort(404, message="item not found")


@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "store deleted"}
    except KeyError:
        abort(404, message="store not found")


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}
