# 🎯 Number Guessing Game

A simple Python number guessing game where the computer randomly selects a number and the player tries to guess it. The game provides hints based on how close the guess is to the correct number and displays a fancy congratulatory message upon winning using **PyFiglet**.

## 🚀 Features

* Random number generation using Python's `random` module.
* Dynamic hints based on the distance from the correct number.
* Encourages the player with proximity-based feedback.
* ASCII-art victory message using `pyfiglet`.
* Beginner-friendly Python project.

## 📋 How It Works

1. The computer generates a random number between **1** and the specified upper limit.
2. The player enters a guess.
3. The game compares the guess with the secret number and provides hints:

### If the guess is too low:

* Difference > 10 → **"Never gonna' get it.... Way too low"**
* Difference between 6 and 9 → **"Try again .... Still low"**
* Difference ≤ 5 → **"Just gonna get it...."**

### If the guess is too high:

* Difference > 10 → **"Never gonna' get it.... Way too High!!!!"**
* Difference between 6 and 9 → **"Try again .... Still high!!"**
* Difference ≤ 5 → **"Just gonna get it...."**

### Correct Guess

When the player guesses the correct number, a congratulatory ASCII-art banner is displayed.
## 🛠 Requirements

* Python 3.x
* PyFiglet

Install PyFiglet using:

```bash
pip install pyfiglet
```

## ▶️ Running the Game

```bash
python guessing_game.py
```

The game starts with a random number between **1 and 50**.

## 📚 Concepts Used

* Functions
* Loops (`while`)
* Conditional Statements (`if`, `elif`, `else`)
* User Input
* Random Number Generation
* Absolute Difference Calculation
* Third-Party Python Libraries

## 🎓 Learning Outcome

This project is great for beginners who want to practice:

* Python syntax
* Problem-solving
* User interaction
* Loop control
* Decision making with nested conditions

## 📄 License

This project is free to use for learning and educational purposes.
.
