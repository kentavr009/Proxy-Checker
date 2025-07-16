import requests

# Список прокси в формате ip:port или user:pass@ip:port
proxies_list = [
    "123.45.67.89:3128",
    "user:pass@111.222.333.444:8080"
    # ... другие прокси
]

for proxy in proxies_list:
    proxy_url = f"http://{proxy}"
    proxies = {"http": proxy_url, "https": proxy_url}
    try:
        # Таймаут в 5 секунд, чтобы не ждать слишком долго
        resp = requests.get("http://ip-api.com/json", proxies=proxies, timeout=5)
        resp.raise_for_status() # Проверка на HTTP ошибки (4xx или 5xx)
        data = resp.json()
        isp = data.get("isp", "Unknown ISP")
        country = data.get("country", "Unknown Country")
        print(f"Proxy {proxy} -> {country}, ISP: {isp}")
    except requests.exceptions.RequestException as e:
        print(f"Proxy {proxy} не работает: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка с прокси {proxy}: {e}")
