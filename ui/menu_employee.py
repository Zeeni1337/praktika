from models.Employee import Employee
from models.Role import Role
from models.Position import Position

def menu_employee():
    """Функция меню управления сотрудниками"""
    while True:
        print("\n=== Меню сотрудников 😘===")
        print("1. Список сотрудников🤑")
        print("2. Добавить сотрудника🤦‍♂️")
        print("0. Назад😢")
        
        choice = input("Выберите пункт:🤞 ").strip()
        
        if choice == "1":
            print("\nСписок сотрудников:")
            for emp in Employee.get_all():
                print(f"{emp.employee_id}: {emp.last_name} {emp.first_name}")
        
        elif choice == "2":
            print("\nДобавление сотрудника:")
            emp = Employee(
                last_name=input("Фамилия: "),
                first_name=input("Имя: "),
                phone_number=input("Телефон: "),
                role_id=1,  # Временное значение
                position_id=1  # Временное значение
            )
            emp.save()
            print("✅ Сотрудник добавлен")
        
        elif choice == "0":
            break
        
        else:
            print("❌ Неверный ввод")

# Важно: убедитесь, что функция существует в глобальной области видимости
if __name__ == "__main__":
    menu_employee()