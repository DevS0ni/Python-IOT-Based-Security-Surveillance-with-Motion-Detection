# Python IOT - Based Security Surveillance with Motion Detection (Raspberry PI Project)

*Project Overview:*
Developed an Internet of Things (IoT) based security system using a Raspberry Pi 4, integrated with a camera module. 
The system detects motion and captures a surveillance video when motion is detected, subsequently sending a security 
alert email with the attached video file to the user.

*TechStack Used:*
Python3

<img width="1003" alt="Screen Shot 2024-02-02 at 1 18 15 PM" src="https://github.com/DevS0ni/Python-IOT-Based-Security-Surveillance-with-Motion-Detection/assets/88739819/ea6f412c-e5b0-44e7-9281-aa8bb897fc08">

*Key Features:*
Motion Detection: Implemented motion detection using a GPIO pin on the Raspberry Pi, allowing the system to identify and respond to movement in the monitored space.
Video Capture: Utilized the Raspberry Pi Camera module to capture a 10-second surveillance video upon detecting motion. The video is stored in H.264 format for efficient storage and processing.
Email Notification: Integrated email functionality to send a security alert to the user's specified email address. The email includes a descriptive subject, body text, and an attached MP4 video file of the detected motion.
Secure Email Transmission: Implemented secure email transmission over the SMTP protocol using the Gmail server. The system requires the user's Gmail credentials for authentication.
File Management: Managed file storage and deletion to optimize storage space. Old video files are removed to ensure the system operates efficiently.

*Technologies Used:*
Raspberry Pi 4: Served as the main processing unit for running the security system.
Raspberry Pi Camera Module: Captured high-quality surveillance videos in real-time.
GPIO (General Purpose Input/Output): Used for motion detection through a connected sensor.
SMTP (Simple Mail Transfer Protocol): Employed for sending security alert emails.
Python Programming Language: Developed the system using Python for GPIO control, camera operation, and email handling.
PIR Sensor: a type of motion sensor that detects infrared radiation emitted by objects within its field of view.
PI Camera: a camera module designed specifically for use with Raspberry Pi single-board computers.
MP4Box: Utilized for converting and processing H.264 video files into MP4 format.

*Setup:*
The system is set up with a Raspberry Pi 4, connected to a camera module and a motion sensor.
The GPIO pin (pin 11) is configured to detect motion changes.
Users need to provide their Gmail credentials and specify the recipient's email address.

*Usage:*
The system continuously monitors the space using the motion sensor.
When motion is detected, the Raspberry Pi Camera captures a 10-second video.
The video is converted to MP4 format using MP4Box for compatibility.
A security alert email is sent to the specified email address, including the attached video file.
Old video files are automatically removed for efficient storage management.

*Impact:*
This IoT-based security system provides an affordable and effective solution for users to monitor and receive timely alerts regarding motion detection in their designated spaces. It enhances security measures with real-time video surveillance and instant email notifications.

*Future Enhancements:*
Future enhancements may include integrating cloud storage for remote video access, implementing real-time monitoring through a web interface, and enhancing the system's scalability for broader applications.
