# Advanced Calculator Application

This project is a sophisticated command-line calculator built with Python. It supports a variety of arithmetic operations, features a robust REPL interface, and incorporates several software engineering best practices and design patterns.

Key features include:
-   **Extended Arithmetic Operations:** Standard operations plus power, root, modulus, integer division, percentage, and absolute difference.
-   **Undo/Redo Functionality:** Manages session history using the Memento Design Pattern.
-   **Automatic Logging & Saving:** Uses the Observer Design Pattern to log all calculations and auto-save history to a CSV file.
-   **Dynamic Help Menu:** Employs the Decorator Design Pattern to automatically generate a help menu.
-   **Configuration Management:** Manages settings through a `.env` file.
-   **Robust Testing:** Includes a comprehensive test suite with over 90% code coverage.
-   **CI/CD Pipeline:** Integrated with GitHub Actions to automate testing on every push.

---
## Installation

To get started with this project, clone the repository and set up the virtual environment.

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd advanced-calculator
    ```

2.  **Create and activate the virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *(On Windows, use `venv\Scripts\activate`)*

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---
## Configuration

The application uses a `.env` file to manage configuration settings.

1.  **Create a `.env` file** in the root directory of the project.
2.  **Add the following variables** to the file. You can change the file paths if you wish.
    ```dotenv
    # .env file
    CALCULATOR_LOG_FILE=calculator.log
    CALCULATOR_HISTORY_FILE=history.csv
    ```

---
## Usage

Run the application from the root directory.

```bash
python3 main.py