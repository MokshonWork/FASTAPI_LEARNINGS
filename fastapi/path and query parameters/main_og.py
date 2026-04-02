from fastapi import FastAPI
import pydantic 
from typing import Optional

#basic and queary parameter

# fastapi is build using the pydantic and it uses it to check whether the input is correct or not
app = FastAPI()


# @app.get("/") #work is to get the req
# # path --> ("/"), get --> operation 
# def index():# path operation function
#     return {"data":"blog list"}# json format


# @app.get("/blog/list")
# def about():
#     return {"data":"this is about page"}
    # return {"about":"this is about page"}
 
@app.get('/blog')
#here the path have the limit otherwise it will not be possible to fetch all data
def index(limit = 10,published : bool = True,sort : Optional[str] =None):
#Optional literally means — "this param may or may not exist"
# only get the 10 published blogs
    if published:
        return {"data": f"{limit} published blog from the db"}
    else:
        return {"data": f"{limit} blog from the db"}



@app.get('/blog/unpublished')
def unpublished():
    return {"blog": "unpublished"}




@app.get('/blog/{id}')
def show(id : int):# cause id will take as input 
    #fetch blog with id = id
    return {"data":id}





#this will show an error cause FAPI read the code line by line
#so when it checked blog/....(can be anything), it checked condition
#in the show func but we actually want to access fuc unpub....
#so, we will shift the un... func before the show fuck


@app.get('/blog/{id}/comments')
def show(id,limit = 10):# cause id will take as input 
    #fetch blog with id = id

    return {"data":{"1","2"}} # output in string but we want in int



