# 🚀 User Data Fetcher

[![API](https://img.shields.io/badge/API-JSONPlaceholder-00A99D?style=for-the-badge&logo=json&logoColor=white)](https://jsonplaceholder.typicode.com/)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-C70D2C?style=for-the-badge&logo=allure&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-C70D2C?style=for-the-badge&logo=allure&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-008CBA?style=for-the-badge&logo=python-requests&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-0052CC?style=for-the-badge&logo=python&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-Up%20to%20Date-brightgreen?style=for-the-badge&logo=dependabot&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Build Passing](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=checkmarx&logoColor=white)
![Coverage](https://img.shields.io/badge/Coverage-100%25-green?style=for-the-badge)
![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000?style=for-the-badge&logo=python&logoColor=white)
![GitHub Stars](https://img.shields.io/github/stars/shlomi10/user-data-fetcher?style=for-the-badge&logo=github)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

## 📝 Overview

A robust Python script for fetching, validating, and processing user data from the JSONPlaceholder API with comprehensive logging and error handling.

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