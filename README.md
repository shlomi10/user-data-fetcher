# 🚀 User Data Fetcher

![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)
![API](https://img.shields.io/badge/API-JSONPlaceholder-green.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📝 Overview

A robust Python script for fetching, validating, and processing user data from the JSONPlaceholder API with comprehensive logging and error handling.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200">
  <rect width="400" height="200" fill="#3498db"/>
  <text x="200" y="100" text-anchor="middle" font-size="40" fill="white" font-family="Arial, sans-serif">
    User Data
  </text>
  <text x="200" y="150" text-anchor="middle" font-size="20" fill="white" font-family="Arial, sans-serif">
    Fetcher
  </text>
</svg>

## ✨ Features

- 🌐 Fetch users from JSONPlaceholder API
- 📧 Email address validation
- 📊 Detailed logging
- 🛡️ Comprehensive error handling
- 🏗️ Object-oriented design

## 🔧 Prerequisites

- Python 3.12+
- pip (Python package manager)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/shlomi10/user-data-fetcher.git
cd user-data-fetcher
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Allure Commandline:
```bash
# On macOS
brew install allure

# On Windows/Linux (with Homebrew)
scoop install allure
```

5. add .env file under utils folder:

add this to .env file
```bash
BASE_URL=https://jsonplaceholder.typicode.com
USERS=/users
```

## 📋 Requirements

requirements.txt:
```
allure_python_commons==2.13.5
pydantic==2.10.6
pytest==8.3.5
PyYAML==6.0.2
email-validator==2.2.0
python-dotenv==1.1.0
Requests==2.32.3
```

## 🖥️ Usage

### Running the Script
```bash
python user_data_fetcher.py
```

### Sample Output
```
ID: 1, Name: Leanne Graham, Email: Sincere@april.biz, Company: Romaguera-Crona
ID: 2, Name: Ervin Howell, Email: Shanna@melissa.tv, Company: Deckow-Crist
```

## 🧪 Testing
PyCharm "Play" Button (GUI)
```bash
How: Click the green "play" icon next to a test/class/module.
Allure Report: Automatically saved to ./reports/
Terminal Command to generate report: allure serve reports
```

Run All Tests
```bash
pytest tests/  # Allure reports auto-generated in ./reports/
```

Run All Tests
```bash
pytest tests/  # Allure reports auto-generated in ./reports/
```

Run Specific Test File:
```bash
pytest tests/test_user.py
```

Run Tests with Markers (e.g., @pytest.mark.functional):
```bash
pytest -m functional
```

Generate the Allure report:
```bash
allure serve reports # Opens browser with interactive report
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

Distributed under the MIT License.

## 🔗 Resources

- [JSONPlaceholder API](https://jsonplaceholder.typicode.com/)
- [Requests Library](https://docs.python-requests.org/)
- [Email Validator](https://github.com/JoshData/python-email-validator)

## 📧 Contact

Project Link: [https://github.com/shlomi10/user-data-fetcher](https://github.com/shlomi10/user-data-fetcher)