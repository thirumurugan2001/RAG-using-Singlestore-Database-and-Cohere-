from rag import rag
from sendMail import send_recruiter_email,send_candidate_alert

# This AzureOpenAIController function is use to Validate the payload data["prompt"] is not empty and string format.
def ragController(Question):
    try:
        if Question != "":
            return rag(Question)
        else:
            return {
                "message":"Invaild data !",
                "statusCode":400,
                "Status":False
            }
    except Exception as e:
        print(f"Error in ragController controller.py file: {str(e)}")
        return {
                "Error":str(e),
                "statusCode":400,
                "message":"Error occurred while processing the request.",
                "Status":False
            }

# This AzureOpenAIController function is use to Validate the payload data["prompt"] is not empty and string format.
def JobOpportunityController(recruiterName,recruiterPhone,recruiterMail,designation,organizationName,JOBDescription):
    try:
        if (recruiterName,recruiterPhone,recruiterMail,designation,organizationName,JOBDescription) != "":
            send_candidate_alert(recruiterName,recruiterPhone,recruiterMail,designation,organizationName,JOBDescription)
            send_recruiter_email(recruiterName,recruiterMail,designation,organizationName)
        else:
            return {
                "message":"Invaild data !",
                "statusCode":400,
                "Status":False
            }
    except Exception as e:
        print(f"Error in ragController controller.py file: {str(e)}")
        return {
                "Error":str(e),
                "statusCode":400,
                "message":"Error occurred while processing the request.",
                "Status":False
            }