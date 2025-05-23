import sqlite3

def get_connection():
    return sqlite3.connect("access_control.db")

def initialize_db():
    """Инициализирует базу данных, создает таблицы"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # Создание таблицы Role
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Role (
            role_id INTEGER PRIMARY KEY AUTOINCREMENT,
            role_name TEXT NOT NULL UNIQUE
        )
        ''')
        
        # Создание таблицы Position
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Position (
            position_id INTEGER PRIMARY KEY AUTOINCREMENT,
            position_name TEXT NOT NULL UNIQUE
        )
        ''')
        
        # Создание таблицы Employee
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employee (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            role_id INTEGER NOT NULL,
            position_id INTEGER NOT NULL,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            phone_number TEXT,
            FOREIGN KEY (role_id) REFERENCES Role(role_id),
            FOREIGN KEY (position_id) REFERENCES Position(position_id)
        )
        ''')
        
        # Создание таблицы Access_Point
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Access_Point (
            access_point_id INTEGER PRIMARY KEY AUTOINCREMENT,
            access_point_name TEXT NOT NULL UNIQUE,
            room TEXT
        )
        ''')
        
        # Создание таблицы Access_Schedule
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Access_Schedule (
            schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            day_of_week TEXT NOT NULL,
            entry_time TEXT NOT NULL,
            exit_time TEXT NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
        )
        ''')
        
        # Создание таблицы Access_Log
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Access_Log (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            access_point_id INTEGER NOT NULL,
            event_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY (employee_id) REFERENCES Employee(employee_id),
            FOREIGN KEY (access_point_id) REFERENCES Access_Point(access_point_id)
        )
        ''')
        
        # Создание таблицы Service
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Service (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_name TEXT NOT NULL UNIQUE,
            description TEXT
        )
        ''')
        
        conn.commit()
        print("База данных успешно инициализирована")
    except Exception as e:
        print(f"Ошибка при инициализации БД: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_db()