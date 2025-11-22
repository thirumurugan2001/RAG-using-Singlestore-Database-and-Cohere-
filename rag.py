from helper import dbconnection, get_embedding
from ConnectChatBot import ConnectChatBot


# Function to get the most relevant answer from the database
def rag(Question):
    try:
        conn=dbconnection()
        cursor=conn.cursor()
        embedding = get_embedding(Question)
        select_query = """SELECT description, dot_product(vector, JSON_ARRAY_PACK("{0}")) AS score FROM famousPlacesIndia ORDER BY score DESC LIMIT 1 """.format(embedding)
        cursor.execute(select_query) 
        rows = cursor.fetchall() 
        if rows:
            response = ConnectChatBot({"Question": rows[0][0] + " . Answer the question: " + Question})
            return {
                "data":response,
                "statusCode":200,
                "message":"Success",
                "Status":True
            }
        else:
            return {
                "statusCode":200,
                "status":False,
                "message":"No relevant information found in the database.",

            }
    except Exception as e:
        print(f"Error in rag function: {str(e)}")
        return {
                "Error":str(e),
                "statusCode":400,
                "message":"Error occurred while processing the request.",
                "Status":False
            }
