# CSVtoReport

**CLI инструмент для генерации отчетов из CSV**

## Быстрый старт

```
poetry run python main.py --report clickbait --files file_examples/*.csv
```

<img width="837" height="368" alt="Снимок экрана — 2026-04-27 в 22 30 19" src="https://github.com/user-attachments/assets/9364d565-e8d6-464c-843c-3d628f208fc1" />

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
