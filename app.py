from flask import Flask

app = Flask(__name__)


stores=[
    {
        'name':'My Store',
        'items':[
            {
                'name':'My Item',
                'price':15.99
            },
            {
                'name':'Your Item',
                'price':10.99
            },
            {
                'name':'His Item',
                'price':20.99
            }   
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores":stores}


@app.post("/stote")
def create_store():
    request_data=request.get_json()
    new_store={"name":request_data["name"]}
    