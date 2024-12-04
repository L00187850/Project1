# This is the module-level docstring.
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


class UserDetails:
    """
Here I have create a class called userDetails.
didn't need an __init__ as I didn't require any arrtibutes.
Inside of the class I have created multiple methods inside of it
providing information on a user such as their basic device information,
the current time, their home directory size, and the last logged in user
to the machine.
    """

    def get_user_info(self):
        """
        This method obtains specific details that are unique to the logged in user.
        What this script does is that it finds the current logged in user, the home directory
        of that user, the operating system its using, the version of OS, the release date of that
        OS and even what architecture of processor is being used.
        """
        user_info = {
            "Username: ": getpass.getuser(),
            "Home Directory: ": os.path.expanduser("~"),
            "Operating System: ": platform.system(),
            "OS Version: ": platform.version(),
            "OS Release Date: ": platform.release(),
            "Processor architecture being used: ": platform.processor()
        }
        return user_info

    def get_current_time(self):
        """
        This method obtains the current time on the machine. It finds each type time such
        as hour, minute, day, week, date, month, and year. In main it then outputs the information
        in a For loop to show each output in its own line.
        """
        now = datetime.now()
        time_info = {
            "Hour": now.strftime("%I"), #This shows it in a 12 hour format.
            "Minute": now.strftime("%M"), #This shows the minutes.
            "Day of Week": now.strftime("%A"), # This shows the day of the week.
            "Date": now.strftime("%d"), # This shows the date of the month.
            "Month": now.strftime("%B"), # This shows the month of the year.
            "Year": now.strftime("%Y")  # This shows the year.
        }
        return time_info

    def get_directory_size(self, path):
        """
        This method calculates the total size of files in the given directory.
        It calculates the size of every sub-directory and then passes the total.
        What is smart about this bit is that instead of calling each folder size,
        it passes on all folders and just provides the total size in bytes.
        """
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    total_size += os.path.getsize(filepath)  # Add the file size to the total
                except OSError:
                    pass  # Ignore files that can't be accessed

        return total_size

    def get_last_login(self):
        """
        This method gives the last login of the currently logged-in user.
        I found a module called subprocess which, when used correctly, 
        could find the last login of a user. there is a command called lastlog 
        which identifies the last login of a user.
        
        The function also checks if it was successful and outputs the result.
        
        I added a try/catch here to give an error if there is no 
        logged in user or the script somehow fails.
        """
        try:
            # First your getting the username of the currently logged in user.
            username = getpass.getuser()
            """
            This block of code below is declaring a varable called result. 
            it uses a module to run an external command (lastlog -u <username>) 
            and gives its output. stdout=subprocess.pip is an argument which then
            gives the standard output (stdout) of the command. 
            This also stops the command being printed in terminal.
            """
            result = subprocess.run(['lastlog', '-u', username], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True, check=True)
            if result.returncode == 0:
                last_login_output = result.stdout.strip().splitlines()
                #Here if the length of the last login output is greater than 1,
                # return the second element of that list.
                if len(last_login_output) > 1:
                    return last_login_output[1].strip()
            else:
                return "Not available"
         # If this fails throw an exception.
        except Exception as e:
            return f"Error: {e}"
