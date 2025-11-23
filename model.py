from pydantic import BaseModel

class RAG(BaseModel): 
    Question: str

class JobOpportunity(BaseModel): 
    recruiterName: str
    recruiterPhone: str
    recruiterMail: str
    designation: str
    organizationName: str
    JOBDescription: str   