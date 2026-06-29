# Leave Application Generator

A simple Python command-line application that generates professional leave applications for different types of users.

## Features

* School Student Leave Application (To Principal)
* College Student Leave Application (To HOD)
* Employee Leave Application (To Boss/Manager)
* Interactive menu-based interface
* Automatically formats applications using user-provided details
* Clean and beginner-friendly Python code

## How It Works

The user selects one of the following categories:

1. School Student
2. College Student
3. Working Individual

Based on the selected option, the program collects the required information and generates a formatted leave application.

## Technologies Used

* Python 3
* User Input (`input()`)
* Conditional Statements (`if`, `elif`, `else`)
* Variables
* f-Strings
* Multi-line Strings

## Example

### Menu

```text
Leave Application Generator
1. School Student
2. College Student
3. Working Individual
```

### Sample Output

```text
To,
The Principal,
ABC School

Subject: Application for Leave

Respected Sir/Madam,

I am John Doe, a student of Class 12.
I kindly request leave from 01/07/2026 to 03/07/2026 due to illness.

Thank you.

Yours sincerely,
John Doe
```

## What I Learned

* Taking user input from the terminal
* Working with variables and strings
* Using f-strings for dynamic text generation
* Building menu-driven programs
* Implementing decision-making with conditional statements

## Future Improvements

* Save generated applications as text files
* Add date validation
* Add more application templates
* Create a graphical user interface (GUI)
* Export applications as PDF files

## Run the Project

```bash
git clone <repository-url>
cd leave-application-generator
python main.py
```

## Author

Created as a Python learning project to practice string formatting, user input handling, and conditional logic.
