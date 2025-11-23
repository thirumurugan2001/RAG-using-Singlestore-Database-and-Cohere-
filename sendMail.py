
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

def send_candidate_alert(recruiterName, recruiterPhone, recruiterMail, designation, organizationName, JOBDescription) -> bool:
    try:
        msg = MIMEMultipart()
        msg['From'] = os.getenv("SENDER_MAIL")
        msg['To'] = "thirusubramaniyan2001@gmail.com"
        msg['Subject'] = f"🚨 New Job Opportunity Alert - {organizationName}"

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
                    max-width: 800px;
                    margin: 0 auto;
                    background-color: #000000;
                    border: 1px solid #333;
                }}
                .header {{
                    background-color: #000000;
                    color: #ffffff;
                    padding: 20px;
                    border-bottom: 2px solid #fff;
                }}
                .content {{
                    padding: 20px;
                    background-color: #000000;
                }}
                .section {{
                    margin-bottom: 25px;
                    padding: 15px;
                    background-color: #111111;
                    border: 1px solid #333;
                    border-radius: 5px;
                }}
                .section-title {{
                    color: #ffffff;
                    border-bottom: 1px solid #333;
                    padding-bottom: 10px;
                    margin-bottom: 15px;
                    font-size: 18px;
                    font-weight: bold;
                }}
                .field {{
                    margin-bottom: 10px;
                    display: flex;
                }}
                .field-label {{
                    color: #cccccc;
                    font-weight: bold;
                    width: 200px;
                    flex-shrink: 0;
                }}
                .field-value {{
                    color: #ffffff;
                    flex-grow: 1;
                }}
                .footer {{
                    background-color: #000000;
                    color: #cccccc;
                    padding: 15px;
                    text-align: center;
                    border-top: 1px solid #333;
                    font-size: 12px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 style="margin: 0; color: #ffffff;">🚨 NEW JOB OPPORTUNITY</h1>
                    <p style="margin: 5px 0 0 0; color: #cccccc;">Alert generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
                </div>
                
                <div class="content">
                    
                    <!-- Recruiter Information -->
                    <div class="section">
                        <div class="section-title">📋 Recruiter Information</div>
                        <div class="field">
                            <div class="field-label">Recruiter Name:</div>
                            <div class="field-value">{recruiterName}</div>
                        </div>
                        <div class="field">
                            <div class="field-label">Contact Number:</div>
                            <div class="field-value">{recruiterPhone}</div>
                        </div>
                        <div class="field">
                            <div class="field-label">Email:</div>
                            <div class="field-value">{recruiterMail}</div>
                        </div>
                    </div>
                    
                    <!-- Organization Details -->
                    <div class="section">
                        <div class="section-title">🏢 Organization Details</div>
                        <div class="field">
                            <div class="field-label">Organization Name:</div>
                            <div class="field-value">{organizationName}</div>
                        </div>
                        <div class="field">
                            <div class="field-label">Designation:</div>
                            <div class="field-value">{designation}</div>
                        </div>
                    </div>
                    
                    <!-- Job Description -->
                    <div class="section">
                        <div class="section-title">📝 Job Description</div>
                        <div class="field-value" style="white-space: pre-wrap; background-color: #1a1a1a; padding: 15px; border-radius: 5px;">
                            {JOBDescription}
                        </div>
                    </div>

                </div>

                <div class="footer">
                    This is an automated job alert generated by your AI Job Notifier.
                </div>
            </div>
        </body>
        </html>
        '''

        msg.attach(MIMEText(body, 'html'))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("SENDER_MAIL"), os.getenv("APP_PASSWORD"))
            server.sendmail(os.getenv("SENDER_MAIL"), "thirusubramaniyan2001@gmail.com", msg.as_string())
        print("✅ Candidate alert email sent successfully")
        return True
    except Exception as e:
        print(f"❌ Error sending candidate alert: {str(e)}")
        return False

def send_recruiter_email(recruiterName,recruiterMail,designation,organizationName) -> bool:
    try:
        sender_email = os.getenv("SENDER_MAIL")
        app_password = os.getenv("APP_PASSWORD")
        if not sender_email or not app_password:
            return False
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recruiterMail
        msg["Subject"] = "Thank You for Your Interest - Thirumurugan Subramaniyan"
        professional_networks = [
            {"name": "LinkedIn", "url": "https://www.linkedin.com/in/thirumurugan-subramaniyan-a62351212/"},
            {"name": "GitHub", "url": "https://github.com/thirumurugan2001"},
            {"name": "Portfolio", "url": "https://thirumurugan2001.github.io/Thirumurugan-Portfolio/"}
        ]
        networks_html = "".join([
            f'<li style="margin-bottom: 8px;">'
            f'<a href="{net["url"]}" style="color: #000000; text-decoration: none; font-weight: bold;">{net["name"]}</a>'
            f' - {net["url"]}</li>'
            for net in professional_networks
        ])

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
                    max-width: 700px;
                    margin: 0 auto;
                    background-color: #ffffff;
                    border: 2px solid #000000;
                }}
                .header {{
                    background-color: #000000;
                    color: #ffffff;
                    padding: 30px;
                    text-align: center;
                }}
                .content {{
                    padding: 30px;
                    background-color: #ffffff;
                }}
                .section {{
                    margin-bottom: 25px;
                }}
                .contact-info {{
                    background-color: #f5f5f5;
                    padding: 20px;
                    border: 1px solid #000000;
                    margin: 20px 0;
                }}
                .footer {{
                    background-color: #000000;
                    color: #ffffff;
                    padding: 20px;
                    text-align: center;
                }}
                .signature {{
                    margin-top: 30px;
                    border-top: 1px solid #000000;
                    padding-top: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1 style="margin: 0; font-size: 28px;">THIRUMURUGAN SUBRAMANIYAN</h1>
                    <p style="margin: 5px 0 0 0; font-size: 16px; opacity: 0.9;">AI Research Engineer</p>
                </div>

                <div class="content">
                    <div class="section">
                        <p>Dear {recruiterName},</p>

                        <p>Thank you for reaching out regarding the
                        <strong>{designation}</strong> opportunity at
                        <strong>{organizationName}</strong>.</p>

                        <p>I have received the details and I appreciate your interest.
                        I will review the job description and get back to you shortly.</p>
                    </div>

                    <div class="contact-info">
                        <h3 style="margin-top: 0; color: #000000;">Professional Contact Information</h3>

                        <p><strong>📧 Email:</strong> thirusubramaniyan2001@gmail.com</p>
                        <p><strong>📱 Phone:</strong> +91 7339225958</p>
                        <p><strong>📍 Current Location:</strong> Chennai, Tamil Nadu</p>
                        <p><strong>📍 Permanent Location:</strong> Salem, Tamil Nadu</p>
                        <p><strong>🕒 Availability:</strong> Open to work • 1 Month Notice • Ready to relocate</p>
                    </div>

                    <div class="section">
                        <p>I look forward to exploring this opportunity and discussing how my
                        experience in AI, Machine Learning, and software development can
                        contribute to the growth of <strong>{organizationName}</strong>.</p>
                    </div>

                    <div class="signature">
                        <p>Warm regards,</p>
                        <p><strong>Thirumurugan Subramaniyan</strong></p>
                        <p>AI Full Stack Engineer</p>
                    </div>
                </div>

                <div class="footer">
                    <p style="margin: 0; font-size: 12px;">
                        🔗 <a href="https://www.linkedin.com/in/thirumurugan-subramaniyan-a62351212/"
                                style="color: #ffffff;">LinkedIn</a> |
                        🖥 <a href="https://github.com/thirumurugan2001"
                                style="color: #ffffff;">GitHub</a> |
                        🌐 <a href="https://thirumurugan2001.github.io/Thirumurugan-Portfolio/"
                                style="color: #ffffff;">Portfolio</a>
                    </p>
                    <p style="margin: 5px 0 0 0; font-size: 10px; opacity: 0.7;">
                        This is an automated acknowledgement. Feel free to reply to this email.
                    </p>
                </div>
            </div>
        </body>
        </html>
        """

        msg.attach(MIMEText(body, "html"))
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, recruiterMail, msg.as_string())
        print("✅ Recruiter email sent successfully")
        return True
    except Exception as e:
        print(f"❌ Error sending recruiter email: {str(e)}")
        return False
