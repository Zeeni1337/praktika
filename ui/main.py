import os
import sys
from pathlib import Path

# Добавляем путь к проекту в PYTHONPATH
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from database.db_baaza_dannih import initialize_db
from ui.menu import show_main_menu

def setup_paths():
    """Настраивает пути для корректного импорта модулей"""
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(project_root)

def main():
    setup_paths()
    initialize_db()
    
    while True:
        choice = show_main_menu()
        
        if choice == "1":
            from ui.menu_employee import menu_employee
            menu_employee()
        elif choice == "2":
            from ui.menu_orders import menu_orders
            menu_orders()
        elif choice == "0":
            print("Выход из системы...")
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()