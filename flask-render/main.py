# from typing import Optional
# from fastapi import FastAPI, Request
# from pydantic import BaseModel

from flask import Flask, render_template
from flask_cors import CORS, cross_origin

# app = FastAPI()
app = Flask(__name__)

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

@app.route("/", methods=["GET"])
@cross_origin()
def render():
    return render_template('inline-session.html')

# @app.get("/health")
# async def health():
#     return {"message": "OK 200"}

# # GET Request with path parameter
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# # GET Request with query parameter
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#     return fake_items_db[skip : skip + limit]

# # GET Request with both path and an optional query parameter (Default is None, No default value makes the value mandatory)
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# @app.post("/items/")
# async def create_item(item: Item):
#     return item
    

if __name__ == "__main__":
    print(
        (
            "* Loading Flask starting server..."
            "please wait until server has fully started"
        )
    )
    app.config["JSON_SORT_KEYS"] = False
    CORS(app)
    app.config["CORS_HEADERS"] = "Content-Type"
    app.run(host="0.0.0.0", debug=True, port=8080)