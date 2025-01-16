# 90-North
Project Overview

This repository contains solutions for frontend development, Django chat application, and AWS Lambda functions as specified in the assignment.

Frontend Development

Features:

Fixed navbar that remains visible while scrolling.

Three sections below the navbar: a left collapsible menu, a main content area, and a right-side panel.

Footer at the bottom of the page.

JavaScript function to dynamically adjust the page width based on screen size.

How to Run:

Open index.html in a web browser.

Ensure style.css and script.js are in the same directory.

Django Chat Application

Features:

User authentication (sign-up and login).

Collapsible left menu displaying all registered users.

Real-time chat using WebSockets.

Chat history stored in a database.

How to Run:

Navigate to the chat_app directory.

Install dependencies: pip install -r requirements.txt

Run migrations: python manage.py migrate

Start the server: python manage.py runserver

Open the mentioned link in a browser.

AWS Lambda Functions

Features:

Function to add two numbers and return the result.

Function to store a document/PDF in an S3 bucket.

How to Deploy:

Zip the Python file and upload it to AWS Lambda.

Configure the necessary permissions and triggers.

Submission Guidelines

All code is available in this repository.

Follow the directory structure for each component.

Ensure dependencies are installed before running.

Author

Pal.R.Patel
ppalpatel0504@gmail.com
