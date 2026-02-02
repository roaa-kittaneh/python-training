# Python Training Project

This is a simple CLI profile script written in Python.

## Project Overview

This project demonstrates:

- Setting up a Python environment using `venv`.
- Writing a Python script that takes command-line arguments (`sys.argv`).
- Using type hints for better code clarity.
- Formatting code with `black` and linting with `flake8`.
- Managing the project with Git and GitHub.

## How to Run

1. **Clone the repository:**
cd python-training
2. **(Optional) Create and activate a virtual environment:**
   python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Mac/Linux

3. **Install formatting and linting tools (optional, if not installed globally):**
   pip install --upgrade pip
   pip install black flake8

4. **Run the script with your profile information:**
   python profile.py <name> <age> <country>


## Notes

Code is formatted with black and linted with flake8.

Make sure to activate the virtual environment before running the script.

Only the main script profile.py is needed to run the profile card.


