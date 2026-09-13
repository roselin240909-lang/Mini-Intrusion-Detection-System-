# MINI INTRUSION DETECTION SYSTEM🚨

## Description

Mini Intrusion Detection System is a Python program that analyzes security logs and detects suspicious login activity.

## Features

- Reads security log files
- Counts failed login attempts
- Tracks failed attempts by IP address
- Detects suspicious IP addresses
- Finds the highest-risk IP address
- Generates security alerts
- Handles missing log files

## Technologies Used

- Python
- File handling
- Dictionaries
- String processing
- os module
- Basic cybersecurity concepts

## How It Works

1. The program reads the security log file.
2. It finds login attempts that failed.
3. Failed attempts are counted for each IP address.
4. An IP address with 3 or more failed attempts is marked as suspicious.
5. The program identifies the IP address with the most failed attempts.
6. A security alert is displayed for suspicious activity.
