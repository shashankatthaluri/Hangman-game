# 🕹 Hangman Game Project 🕹 

A fun multiplayer hangman game built with Python! 🐍

## 🎮 How to Play

This hangman game can be played by 2 players. One player will think of a secret word, and the other tries to guess it letter by letter before running out of guesses! 

As guesses are made:

- Correct guesses will fill in the matching letters 
- Incorrect guesses deduct a life 
- Run out of lives before guessing the word? You lose!

The first player to correctly guess their opponent's secret word wins the round. Scores are tracked over multiple rounds to determine an overall winner.

## 🛠 Built With

- Python - The programming language used
- Random module - To randomly select secret words
- User input - To get letter guesses from players

## 📝 How It Works

The program:

1. Prompts each player for their name
2. Randomly assigns a secret word from a list  
3. Prints the word with blanks for unknown letters
4. Gets letter guesses and checks them  
5. Updates the printed word and counts lives
6. Checks for a win/loss condition after each turn
7. Switches players and repeats until a winner is determined

## 🚀 Quick Start

To run the game:

1. Install Python 
2. Clone this repo
3. Run `[python hangman.py](Hangman/hangman.py)`
4. Follow the prompts to play!

## 👨‍💻 Author

Created by Atthaluri Shashank - feel free to contact me if you have any other questions!
