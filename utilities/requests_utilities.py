import json
import logging

import allure
import requests
from email_validator import validate_email, EmailNotValidError
from requests.structures import CaseInsensitiveDict
from requests import Response

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RequestsUtilities:

    # Make get request to get status code
    @allure.step("Getting status code for URL: {base_url}{prefix}")
    def get_status_code(self, base_url: str = "", prefix: str = "") -> int:
        try:
            logger.info(f"success getting status code")
            return self.get_call(base_url, prefix).status_code
        except requests.RequestException as e:
            logger.error(f"Error making GET request: {e}")
            return -1  # Indicate failure

    # get the headers
    @allure.step("Fetching headers for URL: {base_url}")
    def get_headers(self, base_url: str = "") -> CaseInsensitiveDict:
        try:
            logger.info(f"success fetching headers")
            return self.get_call(base_url).headers
        except requests.RequestException as e:
            logger.error(f"Error fetching headers: {e}")
            return CaseInsensitiveDict()

    # get the content type
    @allure.step("Fetching content type for URL: {base_url}")
    def get_content_type(self, base_url: str = "") -> str:
        try:
            logger.info(f"success fetching content type")
            return self.get_call(base_url).headers.get('Content-Type', "").split(";")[0]
        except requests.RequestException as e:
            logger.error(f"Error fetching content type: {e}")
            return ""

    # Make the GET request and response json
    @allure.step("Fetching response as JSON from URL: {base_url}{prefix} with params: {params}")
    def get_response_as_json(self, base_url: str = "", prefix: str = "", params: str = "") -> json:
        try:
            logger.info(f"success fetching response")
            return self.get_call(base_url, prefix, params=params).json()
        except requests.RequestException as e:
            logger.error(f"Error fetching response as JSON: {e}")
            return {}

    # Make Get response
    @allure.step("Making GET request to URL: {base_url}{prefix} with params: {params}")
    def get_call(self, base_url: str = "", prefix: str = "", params: str = "") -> Response:
        try:
            logger.info(f"success fetching response")
            return requests.get(base_url + prefix, params=params)
        except requests.RequestException as e:
            logger.error(f"Error fetching response: {e}")
            return Response()

    # Converting a JSON string into a Python dictionary
    @allure.step("Converting JSON string to dictionary")
    def convert_json_to_dict(self, data: str) -> dict:
        try:
            logger.info(f"success parsing JSON string")
            return json.loads(data)
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing JSON string: {e}")
            return {}

    # Validate email format
    @allure.step("Validating email format: {email}")
    def validate_email(self, email: str):
        try:
            validate_email(email, check_deliverability=False)
            logger.info(f"email verified successfully: {email}")
            return True
        except EmailNotValidError as e:
            logger.error(f"Invalid email: {email} - {e}")
            return False