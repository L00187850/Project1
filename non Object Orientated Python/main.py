"""
Name: Philip Stewart
Student Number: L00187850
Date: 04 Dec 2024
Purpose: Retrieve important information on a logged-in user.
"""
from settings.settings import get_user_info, get_current_time, get_directory_size, get_last_login
import os

def main():
    """
    Displays user information, current time, home directory size, and last login details.
    """
    # Fetch details
    user_info = get_user_info()
    time_info = get_current_time()
    home_directory = user_info.get("Home Directory", os.path.expanduser("~"))
    last_login = get_last_login()

    # Display user information
    print("===========================================================")
    print("User Information:")
    for key, value in user_info.items():
        print(f"{key}: {value}")

    # Display time information
    print("\n===========================================================")
    print("Current Time:")
    for key, value in time_info.items():
        print(f"{key}: {value}")

    # Display home directory size
    size_in_bytes = get_directory_size(home_directory)
    print("\n===========================================================")
    print(f"Home Directory Size: {size_in_bytes} bytes")

    # Display last login
    print("\n===========================================================")
    print("Last Login Information:")
    print(f"Last logged in user: {last_login}")

if __name__ == "__main__":
    main()
