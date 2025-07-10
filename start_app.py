import subprocess
import webbrowser
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

subprocess.Popen(["python", "app.py"])

time.sleep(12)

webbrowser.open("http://127.0.0.1:5000")