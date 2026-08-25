# 📧 Email Extractor

A Python automation script that extracts all email addresses from a text file and saves them to a new file, built as part of the **CodeAlpha Python Programming Internship** (Task 3).

## 📌 Overview

This script reads the contents of a `.txt` file, scans it for email addresses using regular expressions, removes duplicates, and saves the unique results into a separate output file.

## ✨ Features

- Reads any `.txt` file provided by the user
- Detects all email addresses using pattern matching, regardless of where they appear in the text
- Removes duplicate email addresses automatically
- Sorts results alphabetically
- Handles missing files and read/write errors gracefully
- Saves extracted emails into a clean, ready-to-use output file

## 🛠️ Concepts Used

- `re` module for pattern matching (regular expressions)
- File handling (`open`, `read`, `write`)
- Set operations for removing duplicates
- Exception handling (`try-except`) for robust file operations

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository or download the script.
3. Place a `.txt` file (containing some email addresses) in the same folder.
4. Run the following command in your terminal:

   python main.py

5. Enter the filename when prompted (e.g. data.txt).
6. The extracted emails will be displayed and saved to extracted_emails.txt.

## 📷 Sample Output

========================================
   EMAIL EXTRACTOR
========================================
Enter the .txt filename to scan (e.g. data.txt): data.txt

Found 3 unique email(s):
  - frenzy123@gmail.com
  - john.doe@example.com
  - support@codealpha.tech
3 email(s) saved to 'extracted_emails.txt'

## 📂 Project Structure

main.py

## 🧑‍💻 Author

Developed by **Muhammad Shehaan Khurram** as part of the CodeAlpha Internship Program.

## 📄 License

This project is open-source and free to use for learning purposes.
