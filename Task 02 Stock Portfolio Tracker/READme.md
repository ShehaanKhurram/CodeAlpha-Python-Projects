# 📊 Stock Portfolio Tracker

A Python application that calculates total investment value based on manually defined stock prices, built as part of the **CodeAlpha Python Programming Internship** (Task 2).

## 📌 Overview

Users can enter stock symbols and the quantity of shares they hold. The program looks up each stock's price from a predefined dictionary, calculates the total investment value, displays a summary, and optionally saves it to a text file.

## ✨ Features

- Displays a list of available stocks and their prices
- Accepts multiple stock entries in a single session
- Validates stock symbols and quantity input
- Automatically combines quantities if the same stock is entered more than once
- Calculates per-stock value and total portfolio investment
- Displays a clean, formatted summary table
- Optionally exports the summary to a personalized .txt file

## 🛠️ Concepts Used

- Dictionaries for stock price lookup and portfolio storage
- Input/output handling with validation
- Basic arithmetic for value calculations
- File handling for exporting results
- Function-based, modular program design

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository or download the script.
3. Run the following command in your terminal:

   python stock_portfolio_tracker.py

4. Enter stock symbols and quantities as prompted. Type `done` when finished.
5. Choose whether to save the summary to a file.

## 📷 Sample Output

========================================
        PORTFOLIO SUMMARY
========================================
Stock   Qty     Price     Value
----------------------------------------
AAPL    10      $180      $1800
TSLA    5       $250      $1250
----------------------------------------
TOTAL INVESTMENT: $3050
========================================

## 📂 Project Structure

stock_portfolio_tracker.py

## 🧑‍💻 Author

Developed by **Muhammad Shehaan Khurram** as part of the CodeAlpha Internship Program.

## 📄 License

This project is open-source and free to use for learning purposes.
