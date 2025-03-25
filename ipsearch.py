import requests
import os

def get_location_by_ip(ip_address):
    # API для определения геолокации по IP
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            city = data.get('city', 'Город не найден')
            country = data.get('country', 'Страна не найдена')
            region = data.get('regionName', 'Регион не найден')
            zipcode = data.get('zip', 'Почтовый индекс не найден')
            latitude = data.get('lat', 'Широта не найдена')
            longitude = data.get('lon', 'Долгота не найдена')
            isp = data.get('isp', 'Провайдер не найден')

            return {
                'city': city,
                'country': country,
                'region': region,
                'zipcode': zipcode,
                'latitude': latitude,
                'longitude': longitude,
                'isp': isp
            }
        else:
            return None, "IP не найден"
    else:
        return None, "Ошибка запроса"

def main():
    RED = "\033[31m"  # ANSI-код для красного
    RESET = "\033[0m"  # Сброс цвета
    GREEN = "\033[32m"
    while True:
        print("\u001b[32mВыберите действие:")  # Зеленый цвет
        print("1. Поиск по IP")  # Зеленый цвет
        print(f"99. Выход\u001b[37m")  # Зеленый цвет
        choice = input("Введите номер действия: ")

        if choice == "1":
            ip_address = input("Введите IP-адрес для поиска города: ")
            location_info = get_location_by_ip(ip_address)

            if location_info:
                print(f"Город: {location_info['city']}, Страна: {location_info['country']}, "
                      f"Регион: {location_info['region']}, Почтовый индекс: {location_info['zipcode']}, "
                      f"Широта: {location_info['latitude']}, Долгота: {location_info['longitude']}, "
                      f"Провайдер: {location_info['isp']}")
            else:
                print(location_info[1])  # Сообщение об ошибке
        elif choice == "99":
            os.system('python main.py')  # Открывает файл main.py
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()