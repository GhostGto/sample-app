from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Deploy py app it's working!!!!!!!"}
