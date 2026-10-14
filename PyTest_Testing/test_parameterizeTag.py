import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubSpot(BaseTest):

    @pytest.mark.parametrize(
        "username, password",
        [
            ("admin@gmail.com", "admin123"),
            ("naveen@gmail.com", "naveen123"),
        ]
    )
    def test_login(self, username, password):

        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)