import os
import logging
from dotenv import load_dotenv
from utilities.requests_utilities import RequestsUtilities

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dot_env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils", ".env"))
load_dotenv(dotenv_path=dot_env_path)

class BaseTest:
    def __init__(self):

        """Initialize environment variables and RequestsUtilities."""

        self.base_url = os.getenv("BASE_URL")
        self.users = os.getenv("USERS")
        self.requests_utils = RequestsUtilities()

        if not self.base_url or not self.users:
            raise ValueError("BASE_URL or USERS is missing from environment variables")

        logger.info(f"BaseTest initialized with Base URL: {self.base_url}")
