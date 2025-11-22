import uvicorn
from model import RAG
from fastapi import FastAPI
from controller import ragController
app = FastAPI()



# API to get the most relevant answer from the database
@app.post("/chatbot/about/")
async def rag(item: RAG):
    try :
        response = ragController(item.Question)
        return response
    except Exception as e:
        return {
            "error": str(e),
            "stratusCode": 500
        }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)