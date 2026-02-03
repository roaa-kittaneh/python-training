# Python Training Project

This is a simple CLI profile script written in Python.

<img width="615" height="118" alt="image" src="https://github.com/user-attachments/assets/4b2ee062-3de0-421c-9f66-b255df91cac4" />
<img width="1350" height="348" alt="Screenshot 2026-02-03 224338" src="https://github.com/user-attachments/assets/62e5d557-5a3d-4514-bdca-da4c3e711579" />



## project Overview
In this training, I implemented a complete development cycle including:

Environment & Tooling: Setting up isolated environments with venv and maintaining code quality using black (formatting) and flake8 (linting).

Core Logic: Building scripts that utilize type hints, command-line arguments (sys.argv), and advanced control flow (truthy/falsy logic and short-circuiting).

Validation & Testing: Implementing robust input validation and error handling (handling TypeError and ValueError) supported by a comprehensive suite of unit tests using pytest.

Version Control: Managing the entire lifecycle through Git/GitHub with a focus on clean commits.

## How to Run

1. **Clone the repository:**
cd python-training
2. **(Optional) Create and activate a virtual environment:**
   python -m venv venv
venv\Scripts\activate    # Windows

3. **Install formatting and linting tools (optional, if not installed globally):**
   pip install --upgrade pip
   pip install black flake8
   pip install pytest

4. ** Project Structure**
   python-training/
├── profile.py                # CLI script using sys.argv & type hints
├── bmi.py                   # BMI Logic with strict input validation
├── test_bmi.py              # Unit tests for BMI calculator
└── venv/                    # Virtual environment (local only)


5. **Run the Scripts:**
   python profile.py [Name] [Age] [Location]

6. **Execute Tests:**
   pytest -v

Only the main script profile.py is needed to run the profile card.


