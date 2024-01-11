import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()

email_sender="carkhe29@gmail.com"
#La contraseña se debe de sacar la configuracion en 2 pasos del correo por el cual se tiene que enviar
#https://myaccount.google.com/u/0/apppasswords
password = os.getenv("PASSWORD")
email_reciver = "carkhe29@gmail.com"


subject = "Folio Activo ---12625931"
body="""
Buen día, La tienda OXXO 10NLA5039P Los Olivos PDS - - - - , 
ubicada en BLVD LOS OLIVOS SIERRA LOS LIRIOS 400 26015 colonia *LOS OLIVOS , 
Piedras Negras, Coahuila, nos reportó lo siguiente Nombre quien reporta: 
TIENDA INTELIGENTE Situación: Temperatura de retorno > -2°C por mas de 30 min 
Equipo: Hielo 4 Ret. Le pedimos atender la solicitud lo antes posible y confirmarnos 
por este medio cuando quede solucionada. El número de ticket es: 12625931 Servicio a 
Clientes OXXO Oficina de Servicios . Prioridad: ALTA
"""
em = EmailMessage()

em["From"] = email_sender
em["To"] = email_sender
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context = context) as smtp:
    smtp.login(email_sender,password)
    smtp.sendmail(email_sender,email_reciver,em.as_string())