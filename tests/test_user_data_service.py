import allure
import pytest
from win32inetcon import HTTP_STATUS_OK
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@allure.epic("api-backend")
@allure.feature("title - backend")
@allure.story("validate backend api")
@pytest.mark.flaky(reruns=1)
class TestUserDataService:

    @pytest.fixture(autouse=True)
    def setup_class(self, initialize):
        """Automatically setup test class with fixtures"""
        self.base_test_instance = initialize
        self.requests_utils = self.base_test_instance.requests_utils
        self.base_url = self.base_test_instance.base_url
        self.users = self.base_test_instance.users

    # Test to check the status code of the response
    @pytest.mark.functional
    @allure.step("Check if status code is 200 OK")
    @pytest.mark.flaky(reruns=1)
    def test_status_code_is_ok(self):
        """
        Test that the users endpoint returns a 200 OK status
        """
        logger.info(f"Base URL from config: {self.base_url}")

        # Call the status code check
        status_code = self.requests_utils.get_status_code(self.base_url + self.users)
        logger.info(f"Status Code: {status_code}")

        # Assertion to validate the status code is 200
        assert status_code == HTTP_STATUS_OK, f"Expected status code 200, but got {status_code}"

    # Test to check the content type of the response
    @pytest.mark.functional
    @allure.step("Check if content type is application/json")
    @pytest.mark.flaky(reruns=1)
    def test_content_type(self):
        """
        Test that the response content type is application/json
        """
        content_type = self.requests_utils.get_content_type(self.base_url + self.users)
        logger.info(f"Content Type: {content_type}")

        # Validate the content type
        assert content_type == 'application/json', f"Expected header to be application/json, but got {content_type}"

    # Validate that all users have correctly formatted emails
    @pytest.mark.functional
    @allure.step("Validate that all users have correctly formatted emails")
    @pytest.mark.flaky(reruns=1)
    def test_valid_emails(self):
        """
        Validate that all users have correctly formatted emails
        """
        resp_users_as_json = self.requests_utils.get_response_as_json(self.base_url + self.users)

        # List to collect invalid emails
        invalid_emails = []
        valid_users = []

        for user in resp_users_as_json:
            email = user.get("email", "")
            user_id = user.get("id")
            name = user.get("name")
            company_name = user.get("company", {}).get("name")

            if self.requests_utils.validate_email(email):
                valid_users.append({
                    'id': user_id,
                    'name': name,
                    'email': email,
                    'company': company_name
                })
                logger.info(f"Valid email: {email} for user ID: {user_id}, Name: {name}, Company: {company_name}")
                print(f"\n ID: {user_id}, Name: {name}, Email: {email}, Company: {company_name}")
            else:
                invalid_emails.append({
                    'id': user_id,
                    'email': email,
                    'name': name
                })
                logger.error(f"Invalid email for user ID {user_id}: {email}")
                print(f"Invalid email for user ID {user_id}: {email}")

        if invalid_emails:
            print("\n=== Invalid Emails ===")
            for invalid_email in invalid_emails:
                print(
                    f"Invalid email for user ID {invalid_email['id']}: {invalid_email['email']} (Name: {invalid_email['name']})")

        # Assertion at the end to fail the test if any invalid emails exist
        assert len(invalid_emails) == 0, f"Found {len(invalid_emails)} invalid emails:\n" + \
                                             "\n".join([f"ID: {email['id']}, Email: {email['email']}" for email in invalid_emails])
