from models.Access_Log import Access_Log

def get_all_access_logs():
    """Возвращает все записи журнала доступа"""
    return Access_Log.get_all()

def get_access_log_by_id(log_id):
    """Возвращает запись журнала по ID"""
    return Access_Log.get_by_id(log_id)

def manage_access_events(order_id):
    """Управление событиями доступа"""
    while True:
        print("\n=== Управление событиями доступа ===")
        logs = get_all_access_logs()
        
        if not logs:
            print("Нет записей в журнале.")
        else:
            for log in logs:
                print(f"{log.log_id}. Сотрудник ID: {log.employee_id} | "
                      f"Точка доступа: {log.access_point_id} | "
                      f"Дата: {log.date} {log.time} | "
                      f"Тип: {'Вход' if log.event_id == 1 else 'Выход'}")

        print("\n1. Добавить запись доступа😶‍🌫️")
        print("2. Удалить запись🤩")
        print("3. Изменить запись✌️")
        print("0. Назад🤯")
        
        choice = input("Выберите действие:🙃 ")

        if choice == "1":
            print("\n=== Новая запись доступа ===")
            try:
                new_log = Access_Log(
                    employee_id=int(input("ID сотрудника: ")),
                    access_point_id=int(input("ID точки доступа: ")),
                    event_id=int(input("Тип события (1-Вход, 2-Выход): ")),
                    date=input("Дата (ГГГГ-ММ-ДД): "),
                    time=input("Время (ЧЧ:ММ): ")
                )
                new_log.save()
                print("✅ Запись добавлена.")
            except ValueError:
                print("❌ Ошибка ввода данных!")

        elif choice == "2":
            try:
                log_id = int(input("Введите ID записи для удаления: "))
                log = get_access_log_by_id(log_id)
                if log:
                    log.delete()
                    print("✅ Запись удалена.")
                else:
                    print("❌ Запись не найдена!")
            except ValueError:
                print("❌ Неверный ID записи!")

        elif choice == "3":
            try:
                log_id = int(input("Введите ID записи для редактирования: "))
                log = get_access_log_by_id(log_id)
                if log:
                    print("\nОставьте поле пустым, чтобы не изменять")
                    new_event = input(f"Новый тип события [{log.event_id}]: ")
                    new_date = input(f"Новая дата [{log.date}]: ")
                    new_time = input(f"Новое время [{log.time}]: ")

                    if new_event: log.event_id = int(new_event)
                    if new_date: log.date = new_date
                    if new_time: log.time = new_time
                    
                    log.save()
                    print("✅ Запись обновлена.")
                else:
                    print("❌ Запись не найдена!")
            except ValueError:
                print("❌ Ошибка ввода данных!")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод!")

def menu_orders():
    """Главное меню работы с заказами"""
    while True:
        print("\n=== Журнал доступа ===")
        print("1. Показать все записи😘")
        print("2. Добавить запись🤯")
        print("3. Удалить запись😱")
        print("4. Управление записями доступа👺")
        print("0. Назад в главное меню🙉")
        
        choice = input("Выберите действие:🦍 ")
        
        if choice == "1":
            logs = get_all_access_logs()
            print("\nВсе записи доступа:")
            for log in logs:
                print(f"{log.log_id}: Сотр.ID {log.employee_id} | "
                      f"Точка {log.access_point_id} | {log.date} {log.time}")

        elif choice == "2":
            print("\n=== Новая запись ===")
            try:
                new_log = Access_Log(
                    employee_id=int(input("ID сотрудника: ")),
                    access_point_id=int(input("ID точки доступа: ")),
                    event_id=int(input("Тип (1-Вход, 2-Выход): ")),
                    date=input("Дата (ГГГГ-ММ-ДД): "),
                    time=input("Время (ЧЧ:ММ): ")
                )
                new_log.save()
                print("✅ Запись добавлена.")
            except ValueError:
                print("❌ Ошибка ввода данных!")

        elif choice == "3":
            try:
                log_id = int(input("ID записи для удаления: "))
                log = get_access_log_by_id(log_id)
                if log:
                    log.delete()
                    print("✅ Запись удалена.")
                else:
                    print("❌ Запись не найдена!")
            except ValueError:
                print("❌ Неверный ID записи!")

        elif choice == "4":
            try:
                order_id = int(input("Введите ID заказа для управления: "))
                manage_access_events(order_id)
            except ValueError:
                print("❌ Неверный ID заказа!")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод!")