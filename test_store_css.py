import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def assert_amount(driver, search_phrase, expected_count):
    """Funkcja wyszukuje frazę i sprawdza, czy liczba wyników jest zgodna z oczekiwaną.
    Args:
        driver: instancja webdrivera Selenium
        search_phrase: fraza do wyszukania
        expected_count: oczekiwana liczba wyników
    """
    search_field = driver.find_element(By.ID, "searchField")

    search_field.clear()
    search_field.send_keys(search_phrase)

    # Poczekaj na pojawienie się pierwszego wyniku wyszukiwania
    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "section>div>div")) > 0)

    # Znajdź wszystkie karty produktów i przypisz do listy
    products_list = driver.find_elements(By.CSS_SELECTOR, "section>div>div")

    actual_count = len(products_list)
    expected_count_int = int(expected_count)

    print(f"\n{'='*60}")
    print(f"Fraza wyszukiwania: '{search_phrase}'")
    print(f"Znaleziono produktów: {actual_count}, Oczekiwano: {expected_count_int}")
    print(f"{'='*60}")

    # Wyświetl informacje o każdym produkcie z listy za pomocą pola text
    print("\nLista znalezionych produktów:\n")
    for index, product in enumerate(products_list, 1):
        product_text = product.text
        print(f"{index}. {product_text}")
        print("-" * 40)

    assert (
        actual_count == expected_count_int
    ), f"Dla frazy '{search_phrase}' oczekiwano {expected_count_int} wyników, a znaleziono {actual_count}"


def test_store(selenium):
    """Główna funkcja testowa sprawdzająca wyszukiwanie produktów w sklepie"""
    selenium.get("https://kodilla.com/pl/test/store")

    # Poczekaj na załadowanie pola wyszukiwania
    wait = WebDriverWait(selenium, 10)
    wait.until(lambda d: d.find_element(By.ID, "searchField"))

    assert_amount(selenium, "Laptop", "3")
    assert_amount(selenium, "Notebook", "2")
    assert_amount(selenium, "Gaming", "1")
    assert_amount(selenium, "New", "1")
    assert_amount(selenium, "School", "1")
    assert_amount(selenium, "Everyone", "1")
    assert_amount(selenium, "Plus", "1")

    print("\n" + "=" * 60)
    print("✓ Wszystkie testy przeszły pomyślnie!")
    print("=" * 60)
