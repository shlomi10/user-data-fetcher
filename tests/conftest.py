import pytest
import logging
import allure
from pathlib import Path

from tests.base_test import BaseTest

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def initialize():
    """Fixture that initializes BaseTest and yields it."""
    base_test_instance = BaseTest()
    yield base_test_instance

# Custom hook to attach logs or screenshots on failure
def pytest_runtest_logreport(report):
    if report.failed:
        logger.error(f"Test {report.nodeid} failed.")
        allure.attach(f"Failure Reason: {report.longrepr}", name="Failure Details",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach("Test failed due to some reason.", name="Failure Log",
                      attachment_type=allure.attachment_type.TEXT)


def pytest_configure(config):
    # 1. Detect project root (your existing code)
    current_file_path = Path(__file__).absolute()
    project_root = current_file_path
    while not (project_root / '.git').exists() and project_root.parent != project_root:
        project_root = project_root.parent
    if not (project_root / '.git').exists():
        project_root = current_file_path.parent.parent

    # 2. Set Allure output dir (override PyCharm's defaults)
    allure_report_dir = project_root / "reports"
    allure_report_dir.mkdir(exist_ok=True)

    # 3. CRITICAL: Force-enable Allure plugin and set dir
    if hasattr(config, "option"):
        config.option.allure_report_dir = str(allure_report_dir)  # Allure-specific
    config.option.alluredir = str(allure_report_dir)  # Pytest-allure adapter

    logger.info(f"Allure reports will be saved to: {allure_report_dir}")


# Optional: Ensure Allure is installed as a plugin
def pytest_sessionstart(session):
    try:
        import allure.pytest_plugin
    except ImportError:
        logger.warning("Allure plugin not installed. Run: pip install allure-pytest")



