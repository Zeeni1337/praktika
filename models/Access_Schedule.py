from database.db_baaza_dannih import get_connection

class Access_Schedule:
    def __init__(self, schedule_id=None, employee_id=None, 
                 day_of_week=None, entry_time=None, exit_time=None):
        self.schedule_id = schedule_id
        self.employee_id = employee_id
        self.day_of_week = day_of_week
        self.entry_time = entry_time
        self.exit_time = exit_time

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if self.schedule_id is None:
                cursor.execute('''
                INSERT INTO Access_Schedule 
                (employee_id, day_of_week, entry_time, exit_time)
                VALUES (?, ?, ?, ?)
                ''', (self.employee_id, self.day_of_week, 
                     self.entry_time, self.exit_time))
                self.schedule_id = cursor.lastrowid
            else:
                cursor.execute('''
                UPDATE Access_Schedule SET
                    employee_id = ?,
                    day_of_week = ?,
                    entry_time = ?,
                    exit_time = ?
                WHERE schedule_id = ?
                ''', (self.employee_id, self.day_of_week,
                     self.entry_time, self.exit_time, self.schedule_id))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при сохранении графика доступа: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Access_Schedule')
            return [Access_Schedule(*row) for row in cursor.fetchall()]
        finally:
            conn.close()