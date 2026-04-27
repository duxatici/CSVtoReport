# CSVtoReport

**CLI инструмент для генерации отчетов из CSV**

## Быстрый старт

```
poetry run python main.py --report clickbait --files file_examples/*.csv
```

## Архитектура

- Использован паттерн Registry для выбора отчёта
- Использован паттерн Strategy для разделения логики отчета
- Реализован общий интерфейс Report[T]
- Логика разделена на слои:

  * `reports/` — отчеты
  * `services/` — работа с данными
  * `models/` — модели данных
  * `main.py` — CLI и orchestration

## Добавить новый отчет
 - Реализовать свой класс с логикой от родительского Report[T]
 - Импортировать отчет в main.py
