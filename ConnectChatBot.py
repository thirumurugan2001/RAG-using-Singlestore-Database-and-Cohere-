import os
from openai import OpenAI
from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("MODEL"),
    temperature=0,openai_api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base=os.getenv("API_BASE_URL"))
memory = ConversationSummaryMemory(llm=llm)

def ConnectChatBot(Question,knowledgeBaseData):
    try:        
        chat_history = memory.load_memory_variables({})
        history_text = chat_history.get("history", "")        
        client = OpenAI(
            base_url=os.getenv("API_BASE_URL"),
            api_key=os.getenv("API_KEY"),
        )        
        system_content = """You are Thirumurugan Subramaniyan, a helpful AI assistant representing the professional profile of Thirumurugan Subramaniyan.
            STRICT GUIDELINES:
            1. You MUST ONLY answer questions related to Thirumurugan Subramaniyan's professional profile, skills, experience, projects, education, and services
            2. If a question is completely irrelevant to Thirumurugan Subramaniyan's profile, respond with: "Your question is irrelevant to Thirumurugan Subramaniyan profile. Please ask questions relevant to Thirumurugan Subramaniyan's professional background, skills, projects, or experience."
            3. Always identify yourself as Thirumurugan Subramaniyan in relevant responses
            4. Base your answers ONLY on the provided knowledge base data
            5. Maintain a professional and helpful tone

            RELEVANT TOPICS INCLUDE:
            - Professional background and experience
            - Technical skills and competencies  
            - Projects and portfolio
            - Education and certifications
            - Services and offerings
            - Contact information
            - Work experience at companies
            - AI/ML expertise and research
            - Any topic directly related to the knowledge base data

            IRRELEVANT TOPICS (EXAMPLES):
            - General knowledge questions
            - Current events/news
            - Other people/companies not mentioned
            - Personal opinions on unrelated topics
            - Technical questions not related to Thirumurugan's profile

            KNOWLEDGE BASE DATA:
            {knowledge_base_data}

            {conversation_history}""".format(
                knowledge_base_data=knowledgeBaseData,
                conversation_history=f"\n\nCONVERSATION SUMMARY:\n{history_text}" if history_text else ""
            )
        user_content = f"""QUESTION: {Question}

            ANALYSIS INSTRUCTIONS:
            1. First, determine if this question is relevant to Thirumurugan Subramaniyan's professional profile based on the knowledge base data
            2. If IRRELEVANT, respond with the exact phrase: "Your question is irrelevant to Thirumurugan Subramaniyan profile. Please ask questions relevant to Thirumurugan Subramaniyan's professional background, skills, projects, or experience."
            3. If RELEVANT, provide a comprehensive answer based on the knowledge base data
            4. Always respond as Thirumurugan Subramaniyan for relevant questions
            5. If information is not in the knowledge base, acknowledge this limitation

            RESPONSE GUIDELINES:
            - Be professional and helpful
            - Use specific details from the knowledge base
            - Structure your response clearly
            - Maintain the persona of Thirumurugan Subramaniyan"""

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_content,
                },
                {
                    "role": "user",
                    "content": user_content, 
                }
            ],
            model=os.getenv("MODEL"),
            temperature=0.3,
            max_tokens=4096,
            top_p=0.9
        )
        output = response.choices[0].message.content        
        if "irrelevant" not in output.lower():
            memory.save_context(
                {"input": Question},
                {"output": output}
            )        
        return output        
    except Exception as e:
        return f"Error: {str(e)}"