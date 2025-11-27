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

class GeneralContact(BaseModel): 
    Name: str
    ContactNumber: str
    ContactMail: str
    Query: str

class ClientContact(BaseModel): 
    ClientName: str
    ClientPhone: str
    ClientMail: str
    OrganizationType: str
    OrganizationName: str
    OrganizationLocation: str
    TechStack:list
    ProjectDescription: str
    Timeline: str
    Budget: str
