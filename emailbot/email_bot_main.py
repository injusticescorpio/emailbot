import smtplib
import pyttsx3
import speech_recognition as sr
from email.message import EmailMessage
listener=sr.Recognizer()
engine=pyttsx3.init()
def email_list(name):

    dict1={
        'arjun':'arjunpyromancer@gmail.com',
        'dennis':'denz8572@gmail.com',
        'arista':"arista.assistant@gmail.com",
        }
    return dict1[name]
def talk(text):
    engine.say(text)
    engine.runAndWait()
def record_audio():
    with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            voice_data=''
            try:
                voice_data=listener.recognize_google(voice)#convert audio to voice using google api
            except sr.UnknownValueError:
                print("sorry that didn't come up right please try again")
            except sr.RequestError:
                print('sorry my speech server is down')
            return voice_data


def get_email_info():
    talk('To whom you want to send email')
    name=record_audio()
    print(name)
    e_mail=email_list(name.lower())
    print(e_mail)
    talk('Please enter the body of the messsage')
    body=record_audio()
    print(body)
    talk('Please enter the subject of the messsage')
    subject = record_audio()
    print(subject)
    send_email(e_mail,body,subject)

def send_email(e_mail,body,subject):
    #creating server
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('provide email','provide password')
    # server.sendmail('infernoarju@gmail.com','denz8572@gmail.com','Hi Dennis Iam Arjun messaging from Python :)')
    email = EmailMessage()
    email['From'] = 'infernoarju2000@gmail.com'
    email['To'] =e_mail
    email['Subject'] = subject
    email.set_content(body)
    server.send_message(email)
get_email_info()