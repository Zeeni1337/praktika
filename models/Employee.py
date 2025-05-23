from database.db_baaza_dannih import get_connection

class Employee:
    def __init__(self, employee_id=None, role_id=None, position_id=None,
                 last_name=None, first_name=None, middle_name=None, phone_number=None):
        self.employee_id = employee_id
        self.role_id = role_id
        self.position_id = position_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone_number = phone_number

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if self.employee_id is None:
                cursor.execute('''
                INSERT INTO Employee 
                (role_id, position_id, last_name, first_name, middle_name, phone_number)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (self.role_id, self.position_id, self.last_name, 
                     self.first_name, self.middle_name, self.phone_number))
                self.employee_id = cursor.lastrowid
            else:
                cursor.execute('''
                UPDATE Employee SET
                    role_id = ?,
                    position_id = ?,
                    last_name = ?,
                    first_name = ?,
                    middle_name = ?,
                    phone_number = ?
                WHERE employee_id = ?
                ''', (self.role_id, self.position_id, self.last_name,
                     self.first_name, self.middle_name, self.phone_number, self.employee_id))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при сохранении сотрудника: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Employee')
            return [Employee(*row) for row in cursor.fetchall()]
        finally:
            conn.close()

# Добавляем функцию для совместимости
def get_all_employees():
    return Employee.get_all()