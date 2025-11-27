import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def send_project_alert_to_you(ClientName: str,ClientPhone: str,ClientMail: str,OrganizationType: str,OrganizationName: str,OrganizationLocation: str,TechStack: list,ProjectDescription: str,Timeline: str,Budget: str) -> bool:
    """
    Send alert email to you when a client submits a project inquiry
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = os.getenv("SENDER_MAIL")
        msg['To'] = "thirusubramaniyan2001@gmail.com"
        msg['Subject'] = f"🚀 New Project Inquiry - {OrganizationName}"

        # Format tech stack as comma-separated string
        TechStack_formatted = ", ".join(TechStack) if TechStack else "Not specified"

        body = f'''
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #ffffff;
                    background-color: #000000;
                    margin: 0;
                    padding: 20px;
                }}
                .container {{
                    max-width: 900px;
                    margin: 0 auto;
                    background-color: #000000;
                    border: 1px solid #333;
                }}
                .header {{
                    background-color: #000000;
                    color: #ffffff;
                    padding: 25px;
                    border-bottom: 2px solid #fff;
                    text-align: center;
                }}
                .content {{
                    padding: 25px;
                    background-color: #000000;
                }}
                .section {{
                    margin-bottom: 25px;
                    padding: 20px;
                    background-color: #111111;
                    border: 1px solid #333;
                    border-radius: 8px;
                }}
                .section-title {{
                    color: #ffffff;
                    border-bottom: 1px solid #333;
                    padding-bottom: 12px;
                    margin-bottom: 18px;
                    font-size: 20px;
                    font-weight: bold;
                }}
                .field {{
                    margin-bottom: 12px;
                    display: flex;
                }}
                .field-label {{
                    color: #cccccc;
                    font-weight: bold;
                    width: 220px;
                    flex-shrink: 0;
                }}
                .field-value {{
                    color: #ffffff;
                    flex-grow: 1;
                }}
                .tech-stack {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 8px;
                    margin-top: 5px;
                }}
                .tech-tag {{
                    background-color: #1a1a1a;
                    color: #ffffff;
                    padding: 4px 12px;
                    border-radius: 20px;
                    border: 1px solid #333;
                    font-size: 12px;
                }}
                .description-box {{
                    white-space: pre-wrap;
                    background-color: #1a1a1a;
                    padding: 20px;
                    border-radius: 8px;
                    color: #ffffff;
                    line-height: 1.8;
                    border: 1px solid #333;
                }}
                .highlight {{
                    background-color: #2a2a2a;
                    padding: 15px;
                    border-radius: 8px;
                    border-left: 4px solid #ffffff;
                }}
                .footer {{
                    background-color: #000000;
                    color: #cccccc;
                    padding: 20px;
                    text-align: center;
                    border-top: 1px solid #333;
                    font-size: 12px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 style="margin: 0; color: #ffffff; font-size: 32px;">🚀 NEW PROJECT INQUIRY</h1>
                    <p style="margin: 10px 0 0 0; color: #cccccc; font-size: 14px;">
                        Received on {datetime.now().strftime("%Y-%m-%d at %H:%M:%S")}
                    </p>
                </div>
                
                <div class="content">
                    
                    <!-- Client Information -->
                    <div class="section">
                        <div class="section-title">👤 Client Information</div>
                        <div class="field">
                            <div class="field-label">Client Name:</div>
                            <div class="field-value">{ClientName}</div>
                        </div>
                        <div class="field">
                            <div class="field-label">Contact Number:</div>
                            <div class="field-value">{ClientPhone}</div>
                        </div>
                        <div class="field">
                            <div class="field-label">Email Address:</div>
                            <div class="field-value">{ClientMail}</div>
                        </div>
                    </div>
                    
                    <!-- Organization Details -->
                    <div class="section">
                        <div class="section-title">🏢 Organization Details</div>
                        <div class="field">
                            <div class="field-label">Organization Type:</div>
                            <div class="field-value">{OrganizationType}</div>
                        </div>
                        <div class="field">
                            <div class="field-label">Organization Name:</div>
                            <div class="field-value">{OrganizationName}</div>
                        </div>
                        <div class="field">
                            <div class="field-label">Location:</div>
                            <div class="field-value">{OrganizationLocation}</div>
                        </div>
                    </div>

                    <!-- Project Requirements -->
                    <div class="section">
                        <div class="section-title">📋 Project Requirements</div>
                        <div class="field">
                            <div class="field-label">Technology Stack:</div>
                            <div class="field-value">
                                <div class="tech-stack">
                                    {''.join([f'<span class="tech-tag">{tech}</span>' for tech in TechStack]) if TechStack else '<span class="tech-tag">Not specified</span>'}
                                </div>
                            </div>
                        </div>
                        <div class="field">
                            <div class="field-label">Project Timeline:</div>
                            <div class="field-value">{Timeline}</div>
                        </div>
                        <div class="field">
                            <div class="field-label">Budget Range:</div>
                            <div class="field-value">{Budget}</div>
                        </div>
                    </div>

                    <!-- Business Description -->
                    <div class="section">
                        <div class="section-title">📝 Project Description</div>
                        <div class="description-box">
                            {ProjectDescription}
                        </div>
                    </div>

                    <!-- Action Required -->
                    <div class="highlight">
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 24px;">⏰</span>
                            <div>
                                <strong style="color: #ffffff;">Action Required</strong>
                                <p style="margin: 5px 0 0 0; color: #cccccc;">
                                    Please contact the client within 24 hours to discuss project requirements and provide a preliminary proposal.
                                </p>
                            </div>
                        </div>
                    </div>

                </div>

                <div class="footer">
                    This is an automated project inquiry alert generated by your portfolio website.
                </div>
            </div>
        </body>
        </html>
        '''

        msg.attach(MIMEText(body, 'html'))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("SENDER_MAIL"), os.getenv("APP_PASSWORD"))
            server.sendmail(os.getenv("SENDER_MAIL"), "thirusubramaniyan2001@gmail.com", msg.as_string())
        print("✅ Project alert email sent successfully")
        return True
    except Exception as e:
        print(f"❌ Error sending project alert: {str(e)}")
        return False

def send_client_acknowledgement(ClientName: str,ClientMail: str,OrganizationName: str,ProjectDescription: str) -> bool:
    try:
        sender_email = os.getenv("SENDER_MAIL")
        app_password = os.getenv("APP_PASSWORD")
        if not sender_email or not app_password:
            return False
        
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = ClientMail
        msg["Subject"] = "Thank You for Your Project Inquiry - Thirumurugan Subramaniyan"
        description_preview = ProjectDescription[:150] + "..." if len(ProjectDescription) > 150 else ProjectDescription
        body = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #000000;
                    background-color: #ffffff;
                    margin: 0;
                    padding: 20px;
                }}
                .container {{
                    max-width: 750px;
                    margin: 0 auto;
                    background-color: #ffffff;
                    border: 2px solid #000000;
                }}
                .header {{
                    background-color: #000000;
                    color: #ffffff;
                    padding: 35px;
                    text-align: center;
                }}
                .content {{
                    padding: 35px;
                    background-color: #ffffff;
                }}
                .section {{
                    margin-bottom: 25px;
                }}
                .project-summary {{
                    background-color: #f8f8f8;
                    padding: 25px;
                    border: 1px solid #000000;
                    border-radius: 8px;
                    margin: 25px 0;
                }}
                .next-steps {{
                    background-color: #000000;
                    color: #ffffff;
                    padding: 20px;
                    border-radius: 8px;
                    margin: 25px 0;
                }}
                .contact-info {{
                    background-color: #f5f5f5;
                    padding: 20px;
                    border: 1px solid #000000;
                    border-radius: 8px;
                    margin: 20px 0;
                }}
                .footer {{
                    background-color: #000000;
                    color: #ffffff;
                    padding: 25px;
                    text-align: center;
                }}
                .signature {{
                    margin-top: 30px;
                    border-top: 1px solid #000000;
                    padding-top: 25px;
                }}
                .timeline {{
                    display: flex;
                    justify-content: space-between;
                    margin: 20px 0;
                    text-align: center;
                }}
                .timeline-step {{
                    flex: 1;
                    padding: 15px;
                }}
                .timeline-number {{
                    background-color: #000000;
                    color: #ffffff;
                    width: 30px;
                    height: 30px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin: 0 auto 10px;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 style="margin: 0; font-size: 32px;">THANK YOU FOR YOUR PROJECT INQUIRY</h1>
                    <p style="margin: 10px 0 0 0; font-size: 16px; opacity: 0.9;">
                        Your vision meets our technical expertise
                    </p>
                </div>

                <div class="content">
                    <div class="section">
                        <p>Dear <strong>{ClientName}</strong>,</p>

                        <p>Thank you for considering me for your project with <strong>{OrganizationName}</strong>. 
                        I have received your project details and I'm excited about the opportunity to collaborate with you.</p>
                    </div>

                    <div class="project-summary">
                        <h3 style="margin-top: 0; color: #000000; border-bottom: 2px solid #000000; padding-bottom: 10px;">
                            📋 Project Summary
                        </h3>
                        <p><strong>Project Description Preview:</strong></p>
                        <p style="background-color: #ffffff; padding: 15px; border-radius: 5px; border-left: 4px solid #000000;">
                            {description_preview}
                        </p>
                        <p style="margin-top: 15px; font-size: 14px; color: #666;">
                            Full details have been received and are under review.
                        </p>
                    </div>

                    <div class="next-steps">
                        <h3 style="margin-top: 0; color: #ffffff;">🎯 What Happens Next?</h3>
                        <div class="timeline">
                            <div class="timeline-step">
                                <div class="timeline-number">1</div>
                                <div style="font-size: 12px; color: #cccccc;">Project Analysis</div>
                            </div>
                            <div class="timeline-step">
                                <div class="timeline-number">2</div>
                                <div style="font-size: 12px; color: #cccccc;">Proposal Preparation</div>
                            </div>
                            <div class="timeline-step">
                                <div class="timeline-number">3</div>
                                <div style="font-size: 12px; color: #cccccc;">Scheduled Discussion</div>
                            </div>
                        </div>
                        <p style="text-align: center; margin: 0; color: #cccccc;">
                            You will receive a detailed proposal within <strong>24-48 hours</strong>
                        </p>
                    </div>

                    <div class="contact-info">
                        <h3 style="margin-top: 0; color: #000000;">📞 Immediate Contact Information</h3>
                        <p><strong>📧 Email:</strong> thirusubramaniyan2001@gmail.com</p>
                        <p><strong>📱 Phone/WhatsApp:</strong> +91 7339225958</p>
                        <p><strong>💼 LinkedIn:</strong> 
                            <a href="https://www.linkedin.com/in/thirumurugan-subramaniyan-a62351212/" 
                               style="color: #000000; text-decoration: none; font-weight: bold;">
                               Thirumurugan Subramaniyan
                            </a>
                        </p>
                        <p><strong>📍 Availability:</strong> Available for discussion • Flexible scheduling • Quick turnaround</p>
                    </div>

                    <div class="section">
                        <p>I specialize in delivering robust AI solutions, full-stack development, and scalable software architecture. 
                        Your project requirements align well with my expertise, and I'm confident we can create something exceptional together.</p>
                    </div>

                    <div class="signature">
                        <p>Looking forward to our collaboration,</p>
                        <p><strong>Thirumurugan Subramaniyan</strong></p>
                        <p>AI Full Stack Engineer & Technical Consultant</p>
                    </div>
                </div>

                <div class="footer">
                    <p style="margin: 0; font-size: 14px;">
                        🔗 <a href="https://www.linkedin.com/in/thirumurugan-subramaniyan-a62351212/"
                                style="color: #ffffff; text-decoration: none;">LinkedIn</a> | 
                        🖥 <a href="https://github.com/thirumurugan2001"
                                style="color: #ffffff; text-decoration: none;">GitHub</a> | 
                        🌐 <a href="https://thirumurugan2001.github.io/Thirumurugan-Portfolio/"
                                style="color: #ffffff; text-decoration: none;">Portfolio</a>
                    </p>
                    <p style="margin: 10px 0 0 0; font-size: 12px; opacity: 0.7;">
                        This is an automated acknowledgement. For urgent matters, please call +91 7339225958 directly.
                    </p>
                </div>
            </div>
        </body>
        </html>
        """

        msg.attach(MIMEText(body, "html"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, ClientMail, msg.as_string())
        print("✅ Client acknowledgement email sent successfully")
        return True
    except Exception as e:
        print(f"❌ Error sending client acknowledgement: {str(e)}")
        return False