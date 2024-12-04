# User Information Retrieval Script

## Overview
This repository contains two Python scripts (`main.py` and `settings.py`) designed to retrieve and display essential information about the currently logged-in user, their device, and the system's state. The information includes user details, current system time, home directory size, and last login data.

There are two versions of this project:
1. **Object-Oriented Version**: Uses a class-based approach to encapsulate the user information logic.
2. **Plain Version**: Uses functions and avoids object-oriented programming to achieve the same functionality.

### Files

#### 1. `main.py`
- **Author:** Philip Stewart  
- **Student Number:** L00187850  
- **Date:** 04 Dec 2024  
- **Purpose:** This script retrieves important details about the logged-in user, such as their user profile, the current time, and the size of the home directory. It also outputs the last login information.

#### Key Features:
- Retrieves and displays detailed information about the logged-in user:
  - Username
  - Home Directory
  - Operating System
  - Processor Architecture
  - OS Version
  - OS Release Date
- Shows the current time with detailed breakdowns:
  - Hour
  - Minute
  - Day of the week
  - Date of the month
  - Month
  - Year
- Displays the size of the logged-in user's home directory in bytes.
- Shows the most recent login of the user.

#### 2. `settings.py`
- **Author:** Philip Stewart  
- **Student Number:** L00187850  
- **Date:** 04 Dec 2024  
- **Purpose:** The script contains logic to fetch user details, system information, and other related details. There are two versions of this file:
    - **Object-Oriented Version**: Contains a `UserDetails` class with methods to fetch various system data.
    - **Plain Version**: Uses standalone functions to retrieve the same information without classes.

#### Usage:
To run the script, ensure that `settings.py` is in a folder called `settings` and use the following command:
```bash
python main.py

