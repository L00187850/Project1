"""
Name: Philip Stewart
Student Number: L00187850
Date: 04 Dec 2024
Purpose: Retrieve important information on a logged-in user.
"""
import os
import platform
import getpass
from datetime import datetime
import subprocess

def get_user_info():
    """
    Fetch specific details about the logged-in user.
    """
    return {
        "Username": getpass.getuser(),
        "Home Directory": os.path.expanduser("~"),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Processor Architecture": platform.processor()
    }

def get_current_time():
    """
    Fetch the current time details.
    """
    now = datetime.now()
    return {
        "Hour": now.strftime("%I"),
        "Minute": now.strftime("%M"),
        "Day of Week": now.strftime("%A"),
        "Date": now.strftime("%d"),
        "Month": now.strftime("%B"),
        "Year": now.strftime("%Y")
    }

def get_directory_size(path):
    """
    Calculate the total size of files in the given directory.
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
            except OSError:
                pass
    return total_size

def get_last_login():
    """
    Retrieve the last login information for the logged-in user.
    """
    try:
        username = getpass.getuser()
        result = subprocess.run(['lastlog', '-u', username], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True, check=True)
        if result.returncode == 0:
            last_login_output = result.stdout.strip().splitlines()
            if len(last_login_output) > 1:
                return last_login_output[1].strip()
        return "Not available"
    except Exception as e:
        return f"Error: {e}"
