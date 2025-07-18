# Proxy Checker 🌐

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Простой и удобный скрипт для быстрой проверки работоспособности списка прокси-серверов. Он последовательно подключается через каждый прокси и выводит информацию о его геолокации (стране) и интернет-провайдере (ISP).

Недорогие [Резидентные прокси](https://floppydata.com/) 

## ✨ Возможности (Features)

*   **Массовая проверка**: Обрабатывает список прокси любого размера.
*   **Подробная информация**: Для каждого рабочего прокси определяется страна и провайдер.
*   **Поддержка аутентификации**: Работает с прокси формата `ip:port` и `user:pass@ip:port`.
*   **Обработка ошибок**: Информативно сообщает о неработающих прокси и причинах сбоя (таймаут, ошибка подключения и т.д.).
*   **Простота использования**: Легко настраивается путем редактирования одного списка в файле.

## 🚀 Установка (Installation)

Для начала работы с `Proxy Checker` следуйте этим шагам.

1.  Клонируйте репозиторий на свой компьютер:
    ```bash
    git clone https://github.com/ВАШ_НИКНЕЙМ/ВАШ_РЕПОЗИТОРИЙ.git
    cd ВАШ_РЕПОЗИТОРИЙ
    ```
    *(Не забудьте заменить `ВАШ_НИКНЕЙМ` и `ВАШ_РЕПОЗИТОРИЙ` на свои)*

2.  Рекомендуется создать и активировать виртуальное окружение:
    ```bash
    # Для Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Для macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Установите необходимые зависимости из файла `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Как использовать (Usage)

1.  Откройте файл `proxy_checker.py` в любом текстовом редакторе.

2.  Найдите список `proxies_list` и заполните его своими прокси-серверами. Каждый прокси должен быть в кавычках и на новой строке.
    ```python
    # proxy_checker.py

    # Список прокси в формате ip:port или user:pass@ip:port
    proxies_list = [
        "123.45.67.89:3128",
        "user:pass@111.222.333.444:8080",
        # ... добавьте сюда свои прокси
    ]
    ```

3.  Запустите скрипт из вашего терминала:
    ```bash
    python proxy_checker.py
    ```

4.  Скрипт начнет проверку и будет выводить результаты в консоль в реальном времени:
    ```text
    Proxy 123.45.67.89:3128 -> Germany, ISP: Hetzner Online GmbH
    Proxy user:pass@111.222.333.444:8080 не работает: ReadTimeout
    Proxy 98.76.54.32:1080 -> United States, ISP: Comcast Cable
    ```

## 🤝 Содействие (Contributing)

Я приветствую любой вклад в развитие проекта! Если у вас есть идеи по улучшению или вы нашли ошибку, пожалуйста, создайте `Issue` или отправьте `Pull Request`.

1.  Сделайте форк проекта (**Fork**).
2.  Создайте свою ветку для новой функциональности (`git checkout -b feature/AmazingFeature`).
3.  Зафиксируйте свои изменения (`git commit -m 'Add some AmazingFeature'`).
4.  Отправьте изменения в свою ветку (`git push origin feature/AmazingFeature`).
5.  Откройте **Pull Request**.

## 📄 Лицензия (License)

Этот проект распространяется под лицензией MIT. Подробную информацию можно найти в файле `LICENSE`.
