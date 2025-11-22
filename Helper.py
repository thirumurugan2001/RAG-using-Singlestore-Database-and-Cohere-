import os
import singlestoredb as s2
from dotenv import load_dotenv
import pandas as pd
import cohere
load_dotenv()

# Function to get the embedding of the text
def get_embedding(text):
    try:
        token = os.getenv("COHERE_API_KEY")
        co = cohere.Client(token)  
        embedding = co.embed(
            model='embed-english-v3.0', 
            input_type='classification', 
            texts=[text]
            ).embeddings[0] 
        return embedding
    except Exception as e:
        print("Error in getting embedding: ", str(e))
        return None
    
# Function to connect to SingleStore
def dbconnection():
    try :
        conn = s2.connect( 
            host = os.getenv("DB_HOST"), 
            port = os.getenv("PORT"), 
            user =os.getenv("DB_USER"), 
            password = os.getenv("DB_PASSWORD") , 
            database =  os.getenv("DB_NAME")
        )
        print("Connected to SingleStore")
        return conn
    except Exception as e:
        print("Error in connecting to SingleStore: ", str(e))
        return None
    
# Function to create a table in SingleStore
def CreateTable():
    try:
        conn = dbconnection()
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE About(description TEXT,vector blob);")
        conn.commit()
        conn.close()
        return "Table created successfully"
    except Exception as e:
        print("Error in creating table: ", str(e))
        return None

# Function to select data into SingleStore
def selectData():
    try:
        conn = dbconnection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM About")
        data = cursor.fetchall()
        return data
    except Exception as e:
        print("Error in selecting data: ", str(e))
        return None
    
# Function to select data into SingleStore
def dropTable():
    try:
        conn = dbconnection()
        cursor = conn.cursor()
        cursor.execute("DROP TABLE famousPlacesIndia")
        conn.commit()
        return "Table dropped successfully"
    except Exception as e:
        print("Error in selecting data: ", str(e))
        return None

# Function to read the excel file
def read_excel_file():
    try:
        file_path=r'about.xlsx'
        df = pd.read_excel(file_path)
        print("Excel file read successfully")
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None

# Function to insert data into the database
def insert_into_database():
    try:
        conn = dbconnection()
        df = read_excel_file()
        cursor = conn.cursor()
        for index, row in df.iterrows():
            description = row['description']
            vector = get_embedding(description)
            query = """insert into About (description, vector) values ("{0}", JSON_ARRAY_PACK("{1}"))""".format(description, vector)
            cursor.execute(query)
        conn.commit()
        conn.close()
        return "Data inserted successfully"
    except Exception as e:
        print("Error in inserting data:", str(e))
        return None
    
def simple_rag_to_excel(filename="rag_data_simple.xlsx"):
    try : 
        data = [
            { "sno": 1, "description": "Professional Identity: Thirumurugan Subramaniyan is a Software Engineer from Chennai specializing in AI-powered software development. He transforms innovative ideas into intelligent solutions that solve real-world problems with expertise in machine learning and AI systems." },
            { "sno": 2, "description": "Core AI Competencies: Expert in AI and Machine Learning with specialized skills in AI Agents, Autonomous Systems, LLM Fine-tuning, RAG Systems, Computer Vision, and Natural Language Processing using PyTorch and TensorFlow frameworks." },
            { "sno": 3, "description": "Cloud and Development Stack: Proficient in Python and JavaScript programming with expertise in Azure OpenAI services, AWS Bedrock, FastAPI, React development, CI/CD Pipelines, and Microservices Architecture for scalable solutions." },
            { "sno": 4, "description": "Educational Background: Holds Bachelor of Engineering degree in Computer Science and Engineering from Karpagam Academy of Higher Education, Coimbatore, with 83% marks, completed in 2023." },
            { "sno": 5, "description": "Leadership Experience: Former NCC Cadet with strong team collaboration and leadership background, demonstrating exceptional time management, teamwork abilities, and adaptability in challenging environments." },
            { "sno": 6, "description": "Current Role at VPearl Solutions: Working as Application Developer at VPearl Solutions Private Limited, Chennai since January 2025, specializing in developing cutting-edge AI applications and providing innovative solutions." },
            { "sno": 7, "description": "LangTech Project Overview: Developed LangTech, a cutting-edge PaaS platform leveraging advanced AI models for translation services. Created front-end using HTML, CSS, and JavaScript with AI-powered OCR solutions using OpenAI GPT, Google Gemini, and Llama models from January 2025 onwards." },
            { "sno": 8, "description": "Previous Experience at Avasoft: Worked as Software Engineer at Avasoft, Chennai from December 2023 to December 2024, specialized in developing next-generation AI applications and integrated Azure OpenAI Service and AWS Bedrock." },
            { "sno": 9, "description": "Zeb Pulse AI Project: Developed Zeb Pulse, an AI-driven insights platform for AWS Well-Architected Framework Review (March-April 2024). Created front-end with React.js and integrated Azure OpenAI Service with Flask RESTful APIs." },
            { "sno": 10, "description": "Educational RAG Chatbot - LFS: Built LFS web application chatbot (May 2023 - July 2024) for students to clear doubts based on uploaded knowledge, using PostgreSQL, MS SQL databases, and WSL for Terraform code retrieval." },
            { "sno": 11, "description": "CloudGen Drag-and-Drop Platform: Developed CloudGen (September-December 2024), a drag-and-drop application for cloud operations incorporating AWS Bedrock Service for AI responses, cost estimation, and automated deployment." },
            { "sno": 12, "description": "RPA Development Experience: Worked as RPA Developer at ClaySys Technologies, Coimbatore (July-October 2023), creating and maintaining robotic automation workflows using UiPath and RPA Genie with comprehensive documentation." },
            { "sno": 13, "description": "AI Engineering Skills: Comprehensive AI engineering capabilities including LLMs, RAG Systems, Computer Vision, and NLP with practical implementation experience across multiple projects and industries." },
            { "sno": 14, "description": "Full-Stack Development Expertise: Proficient in full-stack development using Python, FastAPI, React, Node.js, and TypeScript for building scalable web applications with modern architecture patterns." },
            { "sno": 15, "description": "Cloud and DevOps Proficiency: Expert in Cloud & DevOps technologies including Azure OpenAI, AWS Bedrock, Docker containerization, and CI/CD pipeline implementation for automated deployments." },
            { "sno": 16, "description": "Data Engineering Capabilities: Strong data engineering skills with SQL, NoSQL, and Vector Databases for efficient data storage, retrieval, and management in AI-powered applications." },
            { "sno": 17, "description": "Automation Testing Skills: Experienced in automation testing using Selenium and Playwright for web application testing, ensuring quality and reliability of software solutions." },
            { "sno": 18, "description": "RPA Engineering Expertise: Skilled in RPA Engineering with UiPath, Automation Anywhere, and Power Automate for creating efficient workflow automation solutions." },
            { "sno": 19, "description": "AI-Powered Cloud Operations: Developed drag-and-drop application simplifying cloud operations with AI-driven architecture generation, Bot3 with RAG integration, automated service creation, and cost estimation." },
            { "sno": 20, "description": "AWS Well-Architected Framework AI: Created RESTful APIs to dynamically streamline AWS Well-Architected Framework Review with AI-driven cloud optimization, automated framework review, and business operation optimization." },
            { "sno": 21, "description": "Student Educational Platform: Built web application for students with RAG integration, LLM integration for intelligent responses, knowledge base upload functionality, and effective doubt resolution system." },
            { "sno": 22, "description": "India Tourism AI Model: Developed RAG and fine-tuning model for tourism recommendations providing intelligent recommendations for famous places in India with location-based insights using fine-tuned LLM models." },
            { "sno": 23, "description": "AI Resume Generator: Created intelligent systems for automated resume creation using DeepSeek AI for resume generation and Ollama models for job description generation with professional automation." },
            { "sno": 24, "description": "Image Recognition System: Built advanced image recognition system using Azure OpenAI to analyze and identify objects, text, and patterns in images with text extraction and multi-format support." },
            { "sno": 25, "description": "Document Translation Application: Developed application translating DOCX files using Google Translate API with DOCX processing, multilingual support, and batch translation functionality." },
            { "sno": 26, "description": "Seal and Stamp Recognition: Created FastAPI-based application for seal and stamp information extraction using OpenAI vision capabilities for document authentication and verification." },
            { "sno": 27, "description": "Azure Pricing Calculator: Built Flask-based web service for Azure pricing calculations automating pricing by scraping Azure Pricing Calculator website using Playwright with real-time data retrieval." },
            { "sno": 28, "description": "Semantic Image Search: Developed FastAPI-based semantic image search using OpenAI's CLIP model with PostgreSQL for similarity search storage and vector embeddings." },
            { "sno": 29, "description": "AI ChatBot with Google: Created AI-powered chatbot using Flask and Azure OpenAI GPT-4o with Google Search API integration, user authentication, and PostgreSQL chat history storage." },
            { "sno": 30, "description": "Zoho CRM Automation: Built desktop application for PDF scraping and content extraction with Zoho CRM API integration for lead management automation and processing capabilities." },
            { "sno": 31, "description": "Advanced OCR Solutions: Developed advanced OCR using OpenAI GPT, Google Gemini, and Llama models with multi-language text recognition, handwritten text capability, and Word document conversion." },
            { "sno": 32, "description": "Voice-Enabled Chatbot: Created voice-enabled chatbot for answering user queries with website content analysis, real-time response generation, and enhanced client interaction." },
            { "sno": 33, "description": "RAG Systems Research: Researching advanced RAG Systems for Enterprise Knowledge with enhanced context understanding, multi-modal capabilities, 40% improved retrieval accuracy, and reduced hallucination rates." },
            { "sno": 34, "description": "Multimodal AI Research: Developing Multimodal AI for Document Understanding by combining text, layout, and visual features achieving 95% accuracy in document classification with real-time processing." },
            { "sno": 35, "description": "LLM Fine-tuning Research: Exploring parameter-efficient fine-tuning methods like LoRA and QLoRA achieving 80% reduction in training memory with faster convergence and maintained 95% performance." },
            { "sno": 36, "description": "Object Detection Research: Developing lightweight object detection models for autonomous systems optimized for edge devices achieving 60 FPS on Jetson Nano with mAP@0.5 of 0.89." },
            { "sno": 37, "description": "Code Generation AI: Building intelligent systems for code generation, bug detection, and automated code review using language models achieving 40% faster review process with accurate predictions." },
            { "sno": 38, "description": "Cross-lingual NLP Research: Researching transfer learning and cross-lingual embeddings for low-resource languages improving performance for 5 languages with zero-shot transfer and cultural context preservation." },
            { "sno": 39, "description": "Python Programming Expertise: Advanced proficiency in Python programming language for AI, machine learning, web development, data analysis, and automation with extensive framework knowledge." },
            { "sno": 40, "description": "JavaScript and TypeScript: Expert in JavaScript and TypeScript development for building modern web applications with type safety and enhanced developer experience." },
            { "sno": 41, "description": "React.js Frontend: Skilled in React.js frontend framework for building interactive user interfaces with component-based architecture and state management." },
            { "sno": 42, "description": "FastAPI Backend Development: Proficient in FastAPI for high-performance backend development with automatic API documentation and async support for scalable applications." },
            { "sno": 43, "description": "Django Framework: Experienced in Django web framework for building robust, secure web applications with ORM, admin interface, and authentication systems." },
            { "sno": 44, "description": "Flask Microframework: Skilled in Flask microframework for building lightweight, flexible web applications and RESTful APIs with minimal overhead." },
            { "sno": 45, "description": "Database Management: Expert in PostgreSQL, MySQL, MongoDB, and MS SQL Server database management systems for efficient data storage and retrieval in applications." },
            { "sno": 46, "description": "Vector Databases: Specialized in Vector databases for AI applications enabling efficient similarity search and semantic retrieval for RAG systems." },
            { "sno": 47, "description": "Azure Cloud Services: Proficient in Azure Cloud services including Azure OpenAI, Azure Blob Storage, and Azure DevOps for building and deploying cloud solutions." },
            { "sno": 48, "description": "AWS Cloud Platform: Experienced with AWS Cloud platform including AWS Bedrock, S3, Lambda, and other services for scalable cloud infrastructure." },
            { "sno": 49, "description": "Docker Containerization: Skilled in Docker containerization for creating consistent development environments and deploying applications across platforms." },
            { "sno": 50, "description": "CI/CD Pipelines: Expert in CI/CD pipeline implementation for automated testing, building, and deployment of applications ensuring code quality and faster releases." },
            { "sno": 51, "description": "REST API Design: Proficient in REST API design and development following best practices for creating scalable, maintainable, and well-documented APIs." },
            { "sno": 52, "description": "Microservices Architecture: Experienced in Microservices architecture for building distributed systems with independent, scalable services communicating through APIs." },
            { "sno": 53, "description": "Agile Methodology: Practiced in Agile development methodology and Scrum framework for iterative development, continuous improvement, and team collaboration." },
            { "sno": 54, "description": "PyTorch Framework: Expert in PyTorch deep learning framework for building, training, and deploying neural networks and AI models." },
            { "sno": 55, "description": "TensorFlow Platform: Skilled in TensorFlow machine learning platform for developing and training machine learning models at scale." },
            { "sno": 56, "description": "Hugging Face Transformers: Proficient in Hugging Face transformers library for NLP tasks, pre-trained models, and fine-tuning capabilities." },
            { "sno": 57, "description": "LangChain Integration: Experienced in LangChain for building LLM applications with chains, agents, and memory for complex AI workflows." },
            { "sno": 58, "description": "OpenAI GPT Models: Skilled in OpenAI GPT models integration for various AI applications including chatbots, content generation, and analysis." },
            { "sno": 59, "description": "Google Gemini API: Proficient in Google Gemini API usage for multimodal AI applications combining text, image, and other data types." },
            { "sno": 60, "description": "Llama Models: Experienced in Llama models implementation for open-source LLM applications with fine-tuning and deployment capabilities." },
            { "sno": 61, "description": "Computer Vision Applications: Expert in Computer Vision applications including object detection, image classification, segmentation, and facial recognition." },
            { "sno": 62, "description": "Natural Language Processing: Skilled in NLP techniques including text classification, named entity recognition, sentiment analysis, and language translation." },
            { "sno": 63, "description": "Machine Learning Algorithms: Proficient in various Machine Learning algorithms for supervised, unsupervised, and reinforcement learning tasks." },
            { "sno": 64, "description": "Data Analysis Tools: Expert in data analysis using Pandas and NumPy for data manipulation, statistical analysis, and visualization." },
            { "sno": 65, "description": "Web Scraping Techniques: Skilled in web scraping techniques using BeautifulSoup, Scrapy, and Selenium for data extraction from websites." },
            { "sno": 66, "description": "Playwright Automation: Proficient in Playwright for browser automation, testing, and web scraping with cross-browser support." },
            { "sno": 67, "description": "Professional Statistics: 3+ years experience in software development, 20+ projects completed successfully, 10+ AI solutions delivered with 100% client satisfaction." },
            { "sno": 68, "description": "Code Quality Achievement: Written 100K+ lines of clean, maintainable code following best practices and coding standards across multiple projects." },
            { "sno": 69, "description": "Availability and Flexibility: Available to join within one month notice period, ready to relocate for right opportunity, open to remote, hybrid, or onsite arrangements." },
            { "sno": 70, "description": "Professional Values: Strong team collaboration skills, leadership background from NCC, continuous learning approach, innovative problem-solving, and scalable system design." },
            { "sno": 71, "description": "Contact Information: Email [thirusubramaniyan2001@gmail.com](mailto:thirusubramaniyan2001@gmail.com), Phone +91-7339225958, Located in Velachery Chennai, Tamil Nadu with permanent address in Salem." },
            { "sno": 72, "description": "Online Profiles: Active on LinkedIn (thirumurugan-subramaniyan), GitHub (thirumurugan2001), CodeChef (thiru2001), HackerRank (thirusubramaniy1), and LeetCode platforms." },
            { "sno": 73, "description": "Service Offerings: AI Research and Development, Machine Learning Model Development, LLM Fine-tuning and Deployment, RAG System Implementation, and Computer Vision Solutions." },
            { "sno": 74, "description": "Development Services: Full-Stack Web Development, Cloud Architecture Design, API Development and Integration, Database Design and Optimization, DevOps and CI/CD Implementation." },
            { "sno": 75, "description": "Consulting Services: Technical Consulting, Project Management, Automation Testing, RPA Development with comprehensive project lifecycle support." },
            { "sno": 76, "description": "Project Methodology: Discovery and Planning (1-2 weeks), Design and Architecture (2-3 weeks), Development (4-12 weeks), Testing and Deployment (1-2 weeks) phases." },
            { "sno": 77, "description": "Development Approach: Agile development approach with continuous integration and deployment, quality assurance testing, performance optimization, and documentation." },
            { "sno": 78, "description": "Industry Experience: Technology and Software Development, Education and E-learning, Healthcare, Finance, E-commerce, Tourism, Government, and Research sectors." },
            { "sno": 79, "description": "Development Tools: Visual Studio Code IDE, Jupyter Notebook, Postman for API testing, pgAdmin for database management, GitLab, Docker, Kubernetes, and Azure DevOps." },
            { "sno": 80, "description": "Design and Management Tools: Figma for UI/UX design, Trello for project management, Jira for agile development, Slack and Microsoft Teams for collaboration." },
            { "sno": 81, "description": "Certifications and Learning: Ongoing professional certifications in AI, Machine Learning, Cloud platforms, Programming languages, DevOps, and Automation technologies." },
            { "sno": 82, "description": "Professional Achievements: Successful enterprise AI deployments, open-source contributions, technical community mentorship, research publications, and project delivery excellence." },
            { "sno": 83, "description": "Core Values: Quality and excellence in delivery, innovation and creativity, client satisfaction focus, continuous improvement, team collaboration, and ethical AI development." },
            { "sno": 84, "description": "Professional Integrity: Transparency in communication, reliability and commitment, professional integrity, and knowledge sharing with stakeholders." },
            { "sno": 85, "description": "Technical Specializations: Large Language Models, Retrieval-Augmented Generation, Vector Databases, AI Model Fine-tuning, Cloud AI Services, and API Development expertise." },
            { "sno": 86, "description": "Architecture Expertise: Microservices Architecture, Data Pipeline Design, Automation Systems, and Performance Optimization for scalable applications." },
            { "sno": 87, "description": "Project Portfolio: Web Applications, Mobile Applications, Desktop Applications, Cloud-native Applications, AI-powered Solutions, Data Analytics Platforms, CRM Systems." },
            { "sno": 88, "description": "Collaboration Experience: Academic Institution Partnerships, Industry Research Collaborations, Open-source Community Contributions, Technical Consulting Services, Knowledge Sharing Initiatives." },
            { "sno": 89, "description": "Research Collaboration: Publication Collaborations, Joint Research Projects, Technology Transfer Programs, Mentorship Programs, Workshop and Training Sessions." },
            { "sno": 90, "description": "Future Aspirations: Advanced AI Research, Cutting-edge Technology Development, Industry Innovation Leadership, Knowledge Expansion, and Professional Growth." },
            { "sno": 91, "description": "Long-term Goals: Community Contribution, Sustainable Technology Solutions, Global Impact Projects, Educational Initiatives, and Research Publications." },
            { "sno": 92, "description": "Work Flexibility: Immediate project start capability, flexible engagement models, full-time project commitment, part-time consulting availability, remote work capability." },
            { "sno": 93, "description": "Engagement Preferences: On-site work readiness, hybrid work model acceptance, international project consideration, long-term project preference, short-term project acceptance." },
            { "sno": 94, "description": "Communication Style: Regular progress updates, transparent communication, comprehensive technical documentation, client collaboration, and effective stakeholder management." },
            { "sno": 95, "description": "Project Management: Team coordination, stakeholder management, project reporting, risk communication, change management, and knowledge transfer processes." },
            { "sno": 96, "description": "Quality Standards: Code quality standards, comprehensive testing methodologies, performance benchmarks, security protocols, and documentation standards implementation." },
            { "sno": 97, "description": "User Focus: User experience focus, scalability considerations, maintenance planning, best practices implementation, and continuous improvement mindset." },
            { "sno": 98, "description": "Innovation Drive: AI technology advancement, solution optimization, process improvement, technology integration, research development, and creative problem-solving." },
            { "sno": 99, "description": "Business Value: Efficiency enhancement, user experience innovation, business value creation through technology, future technology adoption, and sustainable solutions." },
            { "sno": 100, "description": "Professional Summary: Comprehensive AI and software development expertise with proven track record in delivering innovative solutions. Combines technical excellence with strong leadership skills." },
            { "sno": 101, "description": "PDF AI Automation Project: Designed and developed PDF AI automation SaaS web application (April 2025-Present) capable of extracting specific stamp details from PDFs using OCR (Tesseract and Poppler) and AI models including OpenAI's GPT, AWS Bedrock, Ollama, and Hugging Face models." },
            { "sno": 102, "description": "LangTech Translation Features: LangTech is a PaaS web application capable of translating Excel, Word, PDF, and text files, integrating OCR for text extraction and leveraging AI models for accurate multilingual text recognition and translation." },
            { "sno": 103, "description": "LangTech Technical Stack: Developed front-end user interface using HTML, CSS, and React.js. Integrated Python-based RESTful APIs with FastAPI. Implemented PostgreSQL for database management and AWS S3 for secure file storage." },
            { "sno": 104, "description": "PDF Automation Technical Implementation: Front-end developed using HTML, CSS, and React.js. Integrated Python-based RESTful APIs with Flask. Implemented PostgreSQL for database management and Azure Blob for secure file storage." },
            { "sno": 105, "description": "Database Collaboration at VPearl: Worked closely with development team to design and implement database structures. Built APIs using Flask, Sanic, Django, and FastAPI. Implemented responsive designs using HTML, CSS, and JavaScript (React.jsx)." },
            { "sno": 106, "description": "CloudGen Features: Drag-and-drop application enabling users to create services, estimate costs, and deploy to console. Automates cloud processes using AI based on client requirements. Features knowledge base for AI architecture generation and cloud deployment." },
            { "sno": 107, "description": "CloudGen RAG Integration: Integrates Bot3 with Retrieval-Augmented Generation (RAG) for efficient data search and AI-driven responses. Cost estimation for each service seamlessly implemented using Playwright automation." },
            { "sno": 108, "description": "CloudGen Technical Implementation: Front-end created using HTML, CSS, and JavaScript (React.js). Integrated Python and RESTful APIs using Flask. Incorporated AWS Bedrock Service and managed generative AI prompting. Used PostgreSQL and MongoDB databases." },
            { "sno": 109, "description": "LFS Educational Platform: Web application chatbot for students built from December 2023 to February 2024. Implemented RAG by integrating LLMs with data search and AI responses for doubt resolution." },
            { "sno": 110, "description": "LFS Technical Stack: Front-end created using HTML, CSS, and JavaScript (React.js). Integrated Python and RESTful APIs using Flask. Incorporated Azure OpenAI Service and managed generative AI prompting. Used PostgreSQL and MongoDB databases." },
            { "sno": 111, "description": "Zeb Pulse Framework Review: Designed and developed RESTful APIs to dynamically streamline each aspect of AWS Well-Architected Framework Review (July 2023 - December 2024). Enabled businesses to optimize cloud operations with AI-driven insights." },
            { "sno": 112, "description": "Zeb Pulse Technical Stack: Front-end created using HTML, CSS, and JavaScript (React.js). Integrated Python and RESTful APIs using FastAPI. Incorporated Azure OpenAI Service and managed generative AI prompting. Used PostgreSQL and MS SQL databases." },
            { "sno": 113, "description": "RPA Workflow Development: Created and maintained robotic automation workflows using UiPath and RPA Genie at ClaySys Technologies. Tested and troubleshooted automation processes for smooth operation. Documented procedures, configurations, and troubleshooting steps." },
            { "sno": 114, "description": "RPA Team Collaboration: Collaborated with senior RPA developers to optimize and improve automation workflows. Gained hands-on experience in process automation and workflow design during internship period July-October 2023." },
            { "sno": 115, "description": "Academic Performance: Achieved 83% in B.E Computer Science from Karpagam Academy of Higher Education (2023), 72% in HSC from Jayam Matriculation Higher Secondary School (2019), and 80% in SSLC (2017)." },
            { "sno": 116, "description": "Node.js Backend Development: Proficient in Node.js runtime environment for building scalable backend services and APIs. Experience with asynchronous programming and event-driven architecture for high-performance applications." },
            { "sno": 117, "description": "Kubernetes Orchestration: Skilled in Kubernetes orchestration for managing containerized applications at scale. Experience with pod management, service discovery, load balancing, and automated deployments." },
            { "sno": 118, "description": "Git Version Control: Expert in Git version control system for source code management. Proficient in branching strategies, merge workflows, and collaborative development practices." },
            { "sno": 119, "description": "Advanced RAG Implementation: Developed enhanced Retrieval-Augmented Generation systems with improved context understanding and multi-modal capabilities. Achieved 40% improved retrieval accuracy and reduced hallucination rates through multi-source knowledge integration." },
            { "sno": 120, "description": "Document Analysis AI: Combining text, layout, and visual features for comprehensive document analysis and information extraction. Achieved 95% accuracy in document classification with real-time processing capability and cross-format compatibility." },
            { "sno": 121, "description": "Memory-Efficient Fine-tuning: Exploring parameter-efficient fine-tuning methods (LoRA, QLoRA) for adapting large models to specific domains with limited resources. Achieved 80% reduction in training memory requirements with faster convergence and maintained 95% of original performance." },
            { "sno": 122, "description": "Edge Device Object Detection: Development of lightweight object detection models optimized for real-time performance on edge devices. Achieved 60 FPS on Jetson Nano devices with mAP@0.5 of 0.89 and energy-efficient inference." },
            { "sno": 123, "description": "Intelligent Code Analysis: Building intelligent systems for code generation, bug detection, and automated code review using language models. Achieved 40% faster code review process with accurate bug prediction and context-aware code suggestions." },
            { "sno": 124, "description": "Low-Resource Language NLP: Transfer learning and cross-lingual embeddings research for improving NLP capabilities for underrepresented languages. Improved performance for 5 low-resource languages with zero-shot cross-lingual transfer and cultural context preservation." },
            { "sno": 125, "description": "HTML5 and CSS3 Expertise: Advanced knowledge in HTML5 and CSS3 for building responsive, accessible web interfaces. Experience with modern CSS frameworks, flexbox, grid layouts, and CSS animations." },
            { "sno": 126, "description": "Sanic Framework: Proficient in Sanic framework for building fast, asynchronous Python web applications. Experience with async/await patterns and high-performance API development." },
            { "sno": 127, "description": "Redis Cache Implementation: Skilled in Redis for caching, session management, and real-time data processing. Experience with pub/sub messaging and distributed caching strategies." },
            { "sno": 128, "description": "Ollama Model Integration: Experience with Ollama for running large language models locally. Proficient in model deployment, customization, and integration with applications." },
            { "sno": 129, "description": "API Integration Expertise: Comprehensive experience in API integration including RESTful APIs, GraphQL, and third-party service integrations. Skilled in authentication, error handling, and rate limiting." },
            { "sno": 130, "description": "AWS Management Console: Proficient in AWS Management Console for managing cloud resources, monitoring services, and configuring infrastructure. Experience with EC2, S3, Lambda, and other core AWS services." },
            { "sno": 131, "description": "Azure Portal Navigation: Skilled in Azure Portal for resource management, service deployment, and monitoring. Experience with Azure Resource Manager, service configuration, and cost management." },
            { "sno": 132, "description": "Personal Interests and Hobbies: Passionate about gardening, paper craft, and cooking. These creative activities fuel innovation and bring balance to technical work, enhancing problem-solving abilities." },
            { "sno": 133, "description": "NCC Leadership Training: Gained invaluable experience in leadership, time management, and teamwork as senior NCC cadet. Enhanced ability to collaborate effectively with cross-functional teams and adapt quickly to new challenges." },
            { "sno": 134, "description": "Problem-Solving Philosophy: Solving problems by combining logic with creativity, designing solutions that scale and inspire. Focus on building intelligent and impactful digital systems addressing real-world challenges." },
            { "sno": 135, "description": "E-commerce Development: Experience in developing e-commerce platforms with payment gateway integration, inventory management, order processing, and customer relationship management systems." },
            { "sno": 136, "description": "Healthcare Solutions: Developed healthcare applications with patient management, appointment scheduling, medical records management, and HIPAA-compliant data handling." },
            { "sno": 137, "description": "Tourism Technology: Built tourism and hospitality solutions including recommendation systems, booking platforms, and location-based services for enhanced tourist experiences." },
            { "sno": 138, "description": "Financial Technology: Experience in finance and banking solutions with secure transaction processing, fraud detection, compliance management, and financial analytics." },
            { "sno": 139, "description": "Government Projects: Worked on government and public sector projects with emphasis on security, accessibility, transparency, and citizen service delivery." },
            { "sno": 140, "description": "Startup Collaboration: Extensive experience working with startups and entrepreneurship initiatives, providing rapid prototyping, MVP development, and scalable architecture design." },
            { "sno": 141, "description": "Non-profit Solutions: Developed solutions for non-profit organizations focusing on cost-effective implementations, volunteer management, and social impact measurement." },
            { "sno": 142, "description": "Research and Academic Projects: Active participation in research and development projects with academic institutions, contributing to cutting-edge technology exploration and innovation." },
            { "sno": 143, "description": "Security Best Practices: Implementation of security protocols including authentication, authorization, encryption, secure coding practices, and vulnerability assessment." },
            { "sno": 144, "description": "Performance Optimization: Expert in performance optimization techniques including query optimization, caching strategies, load balancing, and resource management for high-traffic applications." },
            { "sno": 145, "description": "Testing Methodologies: Comprehensive knowledge of testing methodologies including unit testing, integration testing, end-to-end testing, and test-driven development practices." },
            { "sno": 146, "description": "Documentation Standards: Strong emphasis on documentation standards including code comments, API documentation, architecture diagrams, and user guides for knowledge transfer." },
            { "sno": 147, "description": "Deployment Automation: Experience in deployment automation using CI/CD tools, infrastructure as code, automated rollback mechanisms, and zero-downtime deployment strategies." },
            { "sno": 148, "description": "Monitoring and Logging: Proficient in monitoring and logging solutions including application performance monitoring, error tracking, log aggregation, and alerting systems." },
            { "sno": 149, "description": "Scalability Architecture: Expertise in designing scalable architectures including horizontal scaling, load balancing, database sharding, and distributed system design." },
            { "sno": 150, "description": "Comprehensive Professional Profile: AI Software Engineer with 3+ years experience, 20+ completed projects, expertise in full-stack development, cloud technologies, AI/ML, and commitment to delivering innovative, scalable, and impactful solutions. Available for immediate engagement with flexible work arrangements and proven track record of 100% client satisfaction across diverse industries." },
        ]
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"Excel file '{filename}' created with {len(data)} records!")
    except Exception as e:
        print(f"Error creating Excel file: {str(e)}")
