import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from socket import gaierror
from email.mime.base import MIMEBase
from datetime import datetime as dt

def email_change():
  
  time_p = dt.now()
  mon = time_p.strftime('%B')
  email_receivers = {'David':'david.sotunbo@e4email.net','Chinenye':'chinenye.okoli@e4email.net','Bisola':'bisola.abegunde@e4email.net','Maxwell':'maxwell.edet@e4email.net','Dr Ime':'ime@e4email.net','Martins': 'enobong.martins@e4email.net','Dashbaords':'e4edashboards@gmail.com','Ukachi': 'ukachi.osisiogu@e4email.net'}
  login= "msdat@e4email.net"
  password = "Zebra555" 
  sender_email = login

  for name,email in email_receivers.items():
          receiver_email = email

          message = MIMEMultipart("alternative")
          message["Subject"] = "NMDR Synchronisation Update"
          message["From"] = sender_email
          message["To"] = receiver_email
          # Add body to email
          
          try:
              body = f' There is change in the data on world from the previous one.Kindly find the attachements to seee the changes'
              message.attach(MIMEText(body, "plain"))
              filename1 = "NewUpdate.csv"  # In same directory as script

            # Open  file in binary mode
              with open(filename1, "rb") as attachment:
                  # Add file as application/octet-stream
                  # Email client can usually download this automatically as attachment
                  part1 = MIMEBase("application", "octet-stream")
                  part1.set_payload(attachment.read())

              # Encode file in ASCII characters to send by email    
              encoders.encode_base64(part1)

              # Add header as key/value pair to attachment part
              part1.add_header(
                  "Content-Disposition",
                  f"attachment; filename= {filename1}",
              )
              message.attach(part1)

              server = smtplib.SMTP('smtp-mail.outlook.com', 587)
              server.starttls()
              server.ehlo()
              server.login(login,password)
              server.sendmail(sender_email, receiver_email, message.as_string())
              server.close()

              # telling the script to report if your message was sent or which errors need to be fixed 
              print(f'Sent to {name}')
          except (gaierror, ConnectionRefusedError):
              print(f'Failed to connect to the server. Bad connection settings? Not sent to {name}, {email}')
          except smtplib.SMTPServerDisconnected:
              print(f'Failed to connect to the server. Wrong user/password?Not sent to {name}, {email}')
          except smtplib.SMTPException as e:
              print(f'SMTP error occurred {str(e)}  Not sent to {name}, {email}')


def email_no_change():
  
  time_p = dt.now()
  mon = time_p.strftime('%B')
  email_receivers = {'David':'david.sotunbo@e4email.net','Ukachi': 'ukachi.osisiogu@e4email.net'}#,'Dr Ime':'ime@ehealth4everyone.com','Jessica':'jessica.isah@e4email.net','David Ayo':'david.ayoola@e4email.net'
  login= "msdat@e4email.net"
  password = "Zebra555" 
  sender_email = login

  for name,email in email_receivers.items():
          receiver_email = email

          message = MIMEMultipart("alternative")
          message["Subject"] = "NMDR Synchronisation Update"
          message["From"] = sender_email
          message["To"] = receiver_email
          # Add body to email
          body = f'There is no chnage in the data for this period from the last time .Regards,Pydata team. '
          message.attach(MIMEText(body, "plain"))
          try:

              server = smtplib.SMTP('smtp-mail.outlook.com', 587)
              server.starttls()
              server.ehlo()
              server.login(login,password)
              server.sendmail(sender_email, receiver_email, message.as_string())
              server.close()

              # telling the script to report if your message was sent or which errors need to be fixed 
              print(f'Sent to {name}')
          except (gaierror, ConnectionRefusedError):
              print(f'Failed to connect to the server. Bad connection settings? Not sent to {name}, {email}')
          except smtplib.SMTPServerDisconnected:
              print(f'Failed to connect to the server. Wrong user/password?Not sent to {name}, {email}')
          except smtplib.SMTPException as e:
              print(f'SMTP error occurred {str(e)}  Not sent to {name}, {email}')
