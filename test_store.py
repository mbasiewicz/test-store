import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def assert_amount(driver, search_phrase, expected_count):
    """Funkcja wyszukuje frazę i sprawdza, czy liczba wyników jest zgodna z oczekiwaną.
    Args:
        driver: instancja webdrivera Selenium
        search_phrase: fraza do wyszukania
        expected_count: oczekiwana liczba wyników
    """
    search_field = driver.find_element(By.XPATH, "//input[@id='searchField']")

    search_field.clear()
    search_field.send_keys(search_phrase)
    time.sleep(1)

    products = driver.find_elements(By.XPATH, "*//div[@class='content']")
    actual_count = len(products)
    expected_count_int = int(expected_count)
    print(
        f"Fraza: '{search_phrase}' - Znaleziono: {actual_count}, Oczekiwano: {expected_count_int}"
    )

    assert (
        actual_count == expected_count_int
    ), f"Dla frazy '{search_phrase}' oczekiwano {expected_count_int} wyników, a znaleziono {actual_count}"


def test_store(selenium):
    """Główna funkcja testowa sprawdzająca wyszukiwanie produktów w sklepie"""
    selenium.get("https://kodilla.com/pl/test/store")
    time.sleep(2)

    assert_amount(selenium, "Laptop", "3")
    assert_amount(selenium, "Notebook", "2")
    assert_amount(selenium, "Gaming", "1")
    assert_amount(selenium, "New", "1")
    assert_amount(selenium, "School", "1")
    assert_amount(selenium, "Everyone", "1")
    assert_amount(selenium, "Plus", "1")

    time.sleep(2)
    selenium.quit()
