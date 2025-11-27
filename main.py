import uvicorn
from fastapi import FastAPI
from model import *
from middleware import setup_cors
from controller import ragController,JobOpportunityController,GeneralContactController,ClientContactController
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

@app.post("/contact/hireme/")
async def rag(item: JobOpportunity):
    try:
        response = JobOpportunityController(item.recruiterName,item.recruiterPhone,item.recruiterMail,item.designation,item.organizationName,item.JOBDescription)
        return response
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

@app.post("/contact/general/")
async def rag(item: GeneralContact):
    try:
        response = GeneralContactController(item.Name,item.ContactNumber,item.ContactMail,item.Query)
        return response
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

@app.post("/contact/client/")
async def rag(item: ClientContact):
    try:
        response = ClientContactController(item.ClientName,item.ClientPhone,item.ClientMail,item.OrganizationType,item.OrganizationName,item.OrganizationLocation,item.TechStack,item.ProjectDescription,item.Timeline,item.Budget,)
        return response
    except Exception as e:
        return {
            "error": str(e),
            "statusCode": 500
        }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)