# Python Selenium Automation Framework

This is a modular, data-driven web automation framework built using **Python**, **Selenium**, and **PyTest**. It follows best practices including Page Object Model (POM), configuration management, logging, and test reporting.

## Project Structure

```
.project root
├── config/
│   └── global.properties       # Configuration for environment data
├── pages/
│   ├── base_page.py            # Common reusable page methods
│   └── login_page.py           # Page Object for Login page
|── reports/
|   └── index.html 
├── tests/
│   └── test_login.py           # Test cases for Login functionality
├── utils/
│   ├── logger.py               # Logger utility
│   └── property_reader.py      # Utility to read property files
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Technologies Used

- **Language:** Python 3.13  
- **Framework:** PyTest  
- **Automation:** Selenium WebDriver  
- **Design Pattern:** Page Object Model (POM)  
- **Utilities:** Logging, Property file reader  
- **Browser Support:** Chrome (default, configurable)

## Test Scenarios

| Test Case                  | Description                                |
|---------------------------|--------------------------------------------|
| `test_valid_login`        | Validates successful login with correct credentials |
| `test_invalid_password`   | Validates error message for wrong password |
| `test_invalid_email`  | Validates error message for wrong email  |

## Configuration

Update the `config/global.properties` file for browser or credentials.

## How to Run Tests

1. **Create a virtual environment:**
   python -m venv .venv

2. **Activate the environment:**
   - Windows:
     .venv\Scripts\activate

3. **Install dependencies:**
   pip install -r requirements.txt

4. **Run the tests:**
   pytest -v tests/

## Reporting
   This project will generate index.html report using pytest-html
