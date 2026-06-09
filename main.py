routes = []

while True:
    print("\n--- ДИСПЕТЧЕРСКАЯ СИСТЕМА ---")
    print("1. Добавить рейс")
    print("2. Показать рейсы")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        driver = input("Водитель: ")
        distance = float(input("Километры: "))

        route = {
            "driver": driver,
            "distance": distance
        }

        routes.append(route)

        print("Рейс добавлен")

    elif choice == "2":
        print("\nСписок рейсов:")

        for route in routes:
            print(
                f"Водитель: {route['driver']} | "
                f"Км: {route['distance']}"
            )

    elif choice == "3":
        break

    else:
        print("Ошибка выбора")