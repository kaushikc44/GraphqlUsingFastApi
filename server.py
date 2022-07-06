from fastapi import FastAPI
from schemas import schema
from starlette.graphql import GraphQLApp
app=FastAPI()

app.add_route("/graphql",GraphQLApp(schema=schema))


@app.get('/')
async def index():
    return {"message":"hello"}