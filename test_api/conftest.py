import pytest
from dotenv import load_dotenv
import os
from test_api.ApiPage import ApiPage

load_dotenv()


@pytest.fixture(scope="session")
def api():
    url = os.getenv("URL")
    return ApiPage(url)
