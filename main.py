import uvicorn
from fastapi import FastAPI
from model import RAG
from controller import ragController
from middleware import setup_cors
app = FastAPI()
setup_cors(app)

@app.post("/chatbot/about/")
async def rag(item: RAG):
    try:
        response = ragController(item.Question)
        return response
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)