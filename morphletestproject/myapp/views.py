from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
import subprocess
import os

def htop(request):
    server_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
    username = os.getlogin()  # Get the system username

    # Run the 'top' command and capture its output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    response = f"""
    Name: Your Full Name
    Username: {username}
    Server Time (IST): {server_time}
    TOP output:
    {top_output}
    """
    return HttpResponse(response)
