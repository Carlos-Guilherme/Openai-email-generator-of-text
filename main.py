import smtplib
import email.message
import openai

openai.api_key = "Your Api"

model_engine = "text-davinci-003"

prompt = "generate a philosophical message based on examples present in stoic and modern philosophy, about modern times"
response = openai.Completion.create(
engine=model_engine,
prompt=prompt,
max_tokens=1024,
temperature=0.5
)
res = response['choices'][0]['text']

def enviar_email():  
    corpo_email = f"""
    <div style="background-color: rgb(33, 221, 180); padding: 10px; border-radius: 15px;">
        <h1 style="font-family: Arial, Helvetica, sans-serif; color: rgb(255, 255, 255);">Message of the day</h1>
        <p style="font-family: Arial, Helvetica, sans-serif; color: rgb(255, 255, 255); font-style: italic;">{res}</p>
    </div>
    """
    msg = email.message.Message()
    msg['Subject'] = "Message of the day"
    msg['From'] = 'your email'
    msg['To'] = 'email to send'
    password = 'Your Password'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()
