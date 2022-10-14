from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Klaviyo Endpoints


@app.get("/klaviyo/metrics")
def get_metrics():
    return {"message": "Hello World"}


@app.get("/klaviyo/list/{list_id}")
def get_list(list_id):
    return {"list_id": list_id}
