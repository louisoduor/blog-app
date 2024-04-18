import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(token: str, email: str) -> None:
    msg = MIMEMultipart("alternative")
    password = os.environ.get("PASSWORD")
    sender = os.getenv("EMAIL")
    link = os.getenv("LINK")
    subject = "Email Verification - AllPulse Blog"
    html_content = f"""
        <html>
<body>
   
    <div style="border:2px solid #4c53c6; padding:10px; border-radius:10px;">
        <h2 style="align-self:center;> AllPulse Blog</h2/>
        <h2 style="align-self:center;">Thank You For Registering With Us.</h2>
        <p>Verify Your Email Address by using the below verification Link.</p>
        <p><b>Verification Link :- </b><strong><a href="{link}/verify/{token}">Click Here</a></strong></p>
        <p>Don't Reply to This Email</p>
    </div>
</body>
</html>
        """
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = email

    part2 = MIMEText(html_content, "html")
    msg.attach(part2)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.login(str(sender), str(password))
    s.sendmail(str(sender), email, msg.as_string())
    s.quit()
