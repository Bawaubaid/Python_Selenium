# Python_Selenium

# Python Selenium Automation Framework

This is a modular, data-driven web automation framework built using **Python**, **Selenium**, and **PyTest**. It follows best practices including Page Object Model (POM), configuration management, logging, and test reporting.

## 📁 Project Structure

```
.
├── config/
│   └── global.properties       # Configuration for environment data
├── pages/
│   ├── base_page.py            # Common reusable page methods
│   └── login_page.py           # Page Object for Login page
├── tests/
│   └── test_login.py           # Test cases for Login functionality
├── utils/
│   ├── logger.py               # Logger utility
│   └── property_reader.py      # Utility to read property files
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## 🚀 Technologies Used

- **Language:** Python 3.x  
- **Framework:** PyTest  
- **Automation:** Selenium WebDriver  
- **Design Pattern:** Page Object Model (POM)  
- **Utilities:** Logging, Property file reader  
- **Browser Support:** Chrome (default, configurable)

## ✅ Test Scenarios

| Test Case                  | Description                                |
|---------------------------|--------------------------------------------|
| `test_valid_login`        | Validates successful login with correct credentials |
| `test_invalid_password`   | Validates error message for wrong password |
| `test_empty_credentials`  | Validates error message for empty email & password |

## ⚙️ Configuration

Update the `config/global.properties` file:
```properties
browser=chrome
email=rahulshettyacademy@gmail.com
password=learning
invalid_password=wrongpassword
```

## 🧪 How to Run Tests

1. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Activate the environment:**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the tests:**
   ```bash
   pytest -v tests/
   ```

## 📋 Reporting (Optional)

To enable HTML reports, install:
```bash
pip install pytest-html
```

Then run:
```bash
pytest --html=report.html
```

## 🤝 Contributions

Contributions, issues and feature requests are welcome.

## 📄 License

This project is licensed under the MIT License.
