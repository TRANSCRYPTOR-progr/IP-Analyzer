# IP Search Module

This module provides IP geolocation lookup functionality using the [IP-API](http://ip-api.com) service. It's designed as a submodule for the main intelligence platform.

## Features

- Geolocation by IP address (city, country, region)
- ISP identification
- Geographic coordinates (latitude/longitude)
- ZIP code lookup
- Simple console interface with color output

## Usage

Called from main menu (option 2 - IP пробив) or can be run independently:

python ipsearch.py
API Reference
get_location_by_ip(ip_address)
Parameters:
ip_address - string containing valid IP address

Returns:
Dictionary with location data or error message

Supported Data Fields:
City

Country

Region

ZIP code

Latitude/Longitude

Internet Service Provider

Requirements
Python 3.8+

requests package

Installation
bash
Copy
pip install requests
Rate Limits
Free tier limitations:

45 requests per minute

No HTTPS (for free tier)

No bulk requests

Integration
Called from main application via:

python
subprocess.run([sys.executable, "ipsearch.py"])
Screenshot
Выберите действие:
1. Поиск по IP
99. Выход
Введите номер действия: 1
Введите IP-адрес для поиска города: 8.8.8.8

Город: Mountain View, Страна: United States, Регион: California
Почтовый индекс: 94035, Широта: 37.4056, Долгота: -122.0775
Провайдер: Google LLC

"Информация - это оружие. Используйте его ответственно."
© ARCHANGEL SOFTWARE 2025.
