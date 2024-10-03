from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/")
async def read_root() -> List[str]:
    return ["Good"]

@app.get("/data", response_model=List[dict])
async def read_data():
    return [
        {"id": 1, "name": "John Doe"}, 
        {"id": 2, "name": "Jane Doe"},
        {"id": 3, "name": "Jane Doe"},

        ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
