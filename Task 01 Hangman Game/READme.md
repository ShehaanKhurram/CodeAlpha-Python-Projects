# 🎮 Hangman Game

A simple text-based Hangman game built in Python as part of the **CodeAlpha Python Programming Internship** (Task 1).

## 📌 Overview

The player tries to guess a hidden word one letter at a time. Each incorrect guess brings the player closer to losing, with a maximum of 6 incorrect guesses allowed before the game ends.

## ✨ Features

- Randomly selects a word from a predefined word list
- Tracks and displays guessed letters
- Validates user input (rejects invalid or duplicate guesses)
- Displays remaining attempts after each turn
- Option to replay without restarting the program

## 🛠️ Concepts Used

- `random` module for word selection
- `while` loops for game flow control
- `if-else` conditionals for guess validation and win/loss logic
- String manipulation for building the word display
- Lists for storing words and guessed letters

## 🚀 How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository or download the script.
3. Run the following command in your terminal:

   python hangman.py

4. Enter one letter at a time when prompted and try to guess the word before running out of attempts.

## 📷 Sample Gameplay

========================================
   WELCOME TO HANGMAN
========================================
You have 6 incorrect guesses allowed.

Word: _ _ _ _ _ _
Wrong attempts: 0/6
Guessed letters: None

Guess a letter: p
✅ Good guess! 'p' is in the word.

## 📂 Project Structure

hangman.py

## 🧑‍💻 Author

Developed by **Muhammad Shehaan Khurram** as part of the CodeAlpha Internship Program.

## 📄 License

This project is open-source and free to use for learning purposes.
