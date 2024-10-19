from flask import Flask
from datetime import datetime
import subprocess
import os

app = Flask(__name__)
@app.route('/htop')
def htop():
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
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

