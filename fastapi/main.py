from fastapi import FastAPI
from enum import Enum
import typing as t
app = FastAPI()


# https://example.com/items/foo -> in our example we only show example.com/
# GET reads data
@app.get("/")
def home_page():
    return {"message": "Hello World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
"""
    Orders matter "users/me" and "user" we need to make sure we order them
"""
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "The current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

class ModelName(str, Enum):
    ALEXNET = "ALEXNET"
    RESNET = "RESNET"
    RENET = "RENET"


@app.get("/models/{model_name}")
# gets model name from our ModelName Class
async def get_model_name(model_name: ModelName):
    if model_name == ModelName.ALEXNET:
        return {"model_name": model_name}
    elif model_name.value == "LENET":
        return {"model_name": "Good choice"}
    else:
        return {"model_name": f"You have selected {model_name.value}"}

@app.get("/files/{file_path:path}")
async def read_file(file_path):
    return {"file_path": file_path}

    ######################################################################
    ###################### QUERY PARAMETERS ##############################
    ######################################################################
    """
    Query parameters - are parameters attached to the end of a URL and
    separated from the URL by a question mark (?). THe sectoin before
    the question mark is the path parameter, and the section after the
    question mark is the query. The path parameter defines the resource
    location, while the query parameter defines, sort, pagination, or 
    filter operations.
    """

dummy_db = [
    {"item_name": "t-shirt"},
    {"item_name": "shoe"},
    {"item_name": "watch"}
]

@app.get("/items/")
async def read_item(skip: int=0, limit: int=10, optional_parameters: t.Optional[int] = None):
    return 0



#### 
@app.get("/uses/{user_id}/items/{item_id}")
async def read_use_item(
    user_id: int, item_id: int, q: t.Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    # if q is NOT empty
    if q:
        item.update({"q": q})
    # if short is TRUE
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


from pydantic import BaseModel

class Book(BaseModel):
    name: str
    author: str
    description: t.Optional[str] =None
    price: float
    
@app.post("/books/")
async def create_item(book: Book):
    return book