import smtplib
import email
import os
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from picamera import PiCamera
from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

# *********************************************** GPIO setup *************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

# *********************************************** Email parameters *************************************************
email_subject = 'Security Alert: Motion Detected'
email_body_text = """\
Hi,
Motion has been detected in your space.
Please check the attached file from the Raspberry Pi security system.
Regards,
Security System
"""
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_USERNAME = 'soni.devk19@gmail.com'
SENDER_PASSWORD = '************' # Hide Intentionally!
RECEIVER_EMAIL = 'onedf3112@gmail.com'

# *********************************************** Video filename and path *************************************************
filename_prefix = "surveillance"
file_extension = ".mp4"
now = datetime.now()
current_datetime = now.strftime("%d-%m-%Y_%H:%M:%S")
filename = filename_prefix + "_" + current_datetime + file_extension
filepath = "/home/pi/python_code/capture/"


def send_security_email():
    message = MIMEMultipart()
    message["From"] = SENDER_USERNAME
    message["To"] = RECEIVER_EMAIL
    message["Subject"] = email_subject

    message.attach(MIMEText(email_body_text, 'plain'))
    attachment = open(filepath + filename, "rb")

    mime_base = MIMEBase('application', 'octet-stream')
    mime_base.set_payload((attachment).read())

    encoders.encode_base64(mime_base)
    mime_base.add_header('Content-Disposition', "attachment; filename= " + filename)

    message.attach(mime_base)
    text = message.as_string()

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    session.ehlo()
    session.starttls()
    session.ehlo()

    session.login(SENDER_USERNAME, SENDER_PASSWORD)
    session.sendmail(SENDER_USERNAME, RECEIVER_EMAIL, text)
    session.quit()
    print("Security Email Sent")


def capture_security_video():
    camera.start_preview()
    camera.start_recording('/home/pi/python_code/capture/new_video.h264')
    camera.wait_recording(10)
    camera.stop_recording()
    camera.stop_preview()


def remove_old_files():
    if os.path.exists("/home/pi/python_code/capture/new_video.h264"):
        os.remove("/home/pi/python_code/capture/new_video.h264")
    else:
        print("File does not exist")

    if os.path.exists(filepath + filename):
        os.remove(filepath + filename)
    else:
        print("File does not exist")


# *************************************************** Initialize Pi Camera **************************************************************************
camera = PiCamera()

# *************************************************** Main code for method calls ********************************************************************
while True:
    motion_status = GPIO.input(11)
    if motion_status == 1:
        print("Motion Detected")
        capture_security_video()
        sleep(2)
        mp4_conversion_status = os.system("MP4Box -add /home/pi/python_code/capture/new_video.h264 /home/pi/python_code/capture/new_video.mp4")
        os.system("mv /home/pi/python_code/capture/new_video.mp4 " + filepath + filename)
        send_security_email()
        sleep(2)
        remove_old_files()
