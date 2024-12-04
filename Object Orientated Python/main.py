"""
Name: Philip Stewart
Student Number: L00187850
Date: 04 Dec 2024
Purpose:Retrieve important information on a logged in user
"""
from settings.settings import UserDetails, os


#Declaring Variables here to run in the rest of the script:
user_details = UserDetails()

# Get user information, time info, and last login details
user_info = user_details.get_user_info()
time_info = user_details.get_current_time()
home_directory = user_info.get("Home Directory: ", None)
last_login = user_details.get_last_login()

def main():
    """
    Displays user information, current time, and profile size.
    It also shows the last login on the device.
    """
    # This part displays user information
    print("===========================================================")
    print("User Information: ")

    for key, value in user_info.items():
        print(f"{key}: {value}")

    # This part displays time information
    print("===========================================================")
    print("")
    print("")
    print("=====================================")
    print("Current Time: " )

    for key, value in time_info.items():
        print(f"{key}: {value}")

    # This part displays the size of the user's home directory, or their profile
    home_directory = os.path.expanduser("~")
    size_in_bytes = user_details.get_directory_size(home_directory)

    print("=====================================")
    print(f"Home Directory Size: {size_in_bytes} bytes")
    print("=====================================")
    # This part displays the most recent used account
    print("=====================================")
    print("Last Login Information: ")

    print(f"Last logged in user: {last_login}")
    print("=====================================")
if __name__ == "__main__":
    main()
