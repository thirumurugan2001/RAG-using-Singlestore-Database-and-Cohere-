from rag import rag
from AutoMail.HiringMail import send_candidate_alert,send_recruiter_email
from AutoMail.GeneralMail import send_contact_alert_to_you,send_acknowledgement_to_user
from AutoMail.ClientMail import send_project_alert_to_you,send_client_acknowledgement

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
            sendCandidateAlert =send_candidate_alert(recruiterName,recruiterPhone,recruiterMail,designation,organizationName,JOBDescription)
            sendRecruiterRmail= send_recruiter_email(recruiterName,recruiterMail,designation,organizationName)
            if sendCandidateAlert and sendRecruiterRmail:
                return {
                    "message":"Job Opportunity details sent successfully!",
                    "statusCode":200,
                    "Status":True
                }
            else:
                return {
                    "message":"Failed to send Job Opportunity details!",
                    "statusCode":500,
                    "Status":False
                }
        else:
            return {
                "message":"Invaild data !",
                "statusCode":400,
                "Status":False
            }
    except Exception as e:
        print(f"Error in JobOpportunityController controller.py file: {str(e)}")
        return {
                "Error":str(e),
                "statusCode":400,
                "message":"Error occurred while processing the request.",
                "Status":False
            }
    
# This AzureOpenAIController function is use to Validate the payload data["prompt"] is not empty and string format.
def GeneralContactController(Name,ContactNumber,ContactMail,Query):
    try:
        if (Name,ContactNumber,ContactMail,Query) != "":
            sendContactAlertToYou =send_contact_alert_to_you(Name,ContactNumber,ContactMail,Query)
            sendAcknowledgementToUser= send_acknowledgement_to_user(Name,ContactMail)
            if sendContactAlertToYou and sendAcknowledgementToUser:
                return {
                    "message":" Contact details sent successfully!",
                    "statusCode":200,
                    "Status":True
                }
            else:
                return {
                    "message":"Failed to send Contact details!",
                    "statusCode":400,
                    "Status":False
                }
        else:
            return {
                "message":"Invaild data !",
                "statusCode":400,
                "Status":False
            }
    except Exception as e:
        print(f"Error in JobOpportunityController controller.py file: {str(e)}")
        return {
                "Error":str(e),
                "statusCode":400,
                "message":"Error occurred while processing the request.",
                "Status":False
            }
    
def ClientContactController(ClientName,ClientPhone,ClientMail,OrganizationType,OrganizationName,OrganizationLocation,TechStack,ProjectDescription,Timeline,Budget):
    try:
        if (ClientName,ClientPhone,ClientMail,OrganizationType,OrganizationName,OrganizationLocation,ProjectDescription,TechStack,Timeline,Budget) != "":
            sendProjectAlertToYou =send_project_alert_to_you(ClientName,ClientPhone,ClientMail,OrganizationType,OrganizationName,OrganizationLocation,TechStack,ProjectDescription,Timeline,Budget)
            sendClientAcknowledgement=send_client_acknowledgement(ClientName,ClientMail,OrganizationName,ProjectDescription)
            if sendProjectAlertToYou and sendClientAcknowledgement:
                return {
                    "message":"Client Contact details processed successfully!",
                    "statusCode":200,
                    "Status":True
                }
            else :
                return {
                    "message":"Failed to process Client Contact details!",
                    "statusCode":400,
                    "Status":False
                }
        else:
            return {
                "message":"Invaild data !",
                "statusCode":400,
                "Status":False
            }
    except Exception as e:
        print(f"Error in ClientContactController controller.py file: {str(e)}")
        return {
                "Error":str(e),
                "statusCode":400,
                "message":"Error occurred while processing the request.",
                "Status":False
            }