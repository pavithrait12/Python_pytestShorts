from selenium import webdriver


def test_insta():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.instagram.com')
    assert driver.title == "Instagram"
    driver.quit()


# def test_gmail():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.get('http://www.gmail.com')
#     assert driver.title == "Gmail"
#     driver.quit()


def test_rediff():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.rediff.com')
    assert driver.title == "Rediff.com: News | Rediffmail | Stock Quotes | Rediff Gurus"
    driver.quit()