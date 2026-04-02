from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional 
import uvicorn # cause i want to change the port

# goal --> post method
app = FastAPI()

class Blog(BaseModel):
    title: str
    body:str
    published_at : Optional[bool]
    
@app.post("/blog")
def create_blog(request:  Blog ): # you also write as blog:  Blog
    return {"data":  f"blog is created with title as {request.title}"}


#note: you can direct manupilate the port number, while running the command
#eg: uvicorn main:app --reload --port 8000

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port=9000)
    # and now just simply run in terminal by writing python main.py
    # it will run on  port 9000
