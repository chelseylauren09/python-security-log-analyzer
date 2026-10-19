
# Python Security Log Analyzer

## Overview

This project is a beginner cybersecurity tool written in Python. It analyzes sample authentication logs to identify repeated failed login attempts that may require further investigation.

## Features

- Reads authentication events from a text file.
- Counts total log events.
- Identifies failed login attempts.
- Counts failed attempts by username and IP address.
- Flags IP addresses with three or more failed login attempts.
- Handles missing log files with a clear error message.

## Technologies Used

- Python 3.13
- Visual Studio Code
- Windows Command Prompt / Terminal
- GitHub

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the analyzer:

   `py analyzer.py`

## Sample Detection Rule

The tool flags an IP address when it has three or more failed login attempts in the sample logs.

This is a basic detection rule for learning purposes. Repeated failures may indicate suspicious activity, but they do not automatically prove an attack.

## Project Files

- `analyzer.py` - The Python script that analyzes the logs.
- `sample_logs.txt` - Fictional authentication log entries used for testing.
- `README.md` - Project documentation.

## Learning Outcomes

Through this project, I practised reading files with Python, processing text, counting events, handling errors, and implementing a basic security detection rule.

## Disclaimer

This project uses fictional log data for educational purposes. It is not a production security monitoring system.
