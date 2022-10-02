# from typing import List
from WP_rewrite import rewrite
# from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://127.0.0.1",
#     "http://127.0.0.1:8000",
# ]


# origins = [
#     "http://127.0.0.1",
#     "http://127.0.0.1:8000",
# ]


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



class Response(BaseModel):
    characters: int
    words: int
    status: str
    text: List

# @app.get("/")
# def read_root(QUERY_STRING):
#     print(QUERY_STRING)
#     a = ' '.join(rewrite(str(QUERY_STRING)))
#     return Response(characters=20, corrections=[], mistakes=[], status="success", text=a, words=4).dict()



#print(rewrite("This is something which i cannot understand at all"))

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    args = request.args
    print(args.get("QUERY_STRING"))
    return Response(characters=20, words=4, status="success", text=rewrite(str(args.get("QUERY_STRING")))).dict()
    
if __name__ == "__main__":
    app.run()