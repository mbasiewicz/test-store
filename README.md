# Test Store - Automatyczne testy wyszukiwania produktów

## Opis

Program testuje wyszukiwanie produktów w sklepie Kodilla używając Selenium i pytest.

## Instalacja

```bash
pip install -r requirements.txt
```

## Uruchomienie

```bash
pytest test_store.py --driver Chrome -v
```

## Co testujemy

| Fraza    | Oczekiwana liczba |
| -------- | ----------------- |
| Laptop   | 3                 |
| NoteBook | 2                 |
| Gaming   | 1                 |
| New      | 1                 |
| School   | 1                 |
| Everyone | 1                 |
| Plus     | 1                 |

## Technologie

- Python 3.x
- Selenium WebDriver
- pytest
- pytest-selenium

## Autor

Zadanie Kodilla (moduł 2.4)
