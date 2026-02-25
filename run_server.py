import webbrowser
import subprocess
import time
import sys
import os

# Change directory to your project folder
project_dir = r"C:\Users\Sydinggod\Desktop\EduMentorAI_Python"
os.chdir(project_dir)

# URL to open
url = "http://127.0.0.1:8000/docs"

# Function to open browser after a short delay
def open_browser():
    time.sleep(2)  # Wait for server to start
    webbrowser.open(url)

# Start the browser in a separate thread
import threading
threading.Thread(target=open_browser).start()

# Start uvicorn server
subprocess.run([sys.executable, "-m", "uvicorn", "main:app", "--reload", "--port", "8000"])