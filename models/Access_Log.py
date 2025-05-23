from database.db_baaza_dannih import get_connection

class Access_Log:
    def __init__(self, log_id=None, employee_id=None, access_point_id=None, 
                 event_id=None, date=None, time=None):
        self.log_id = log_id
        self.employee_id = employee_id
        self.access_point_id = access_point_id
        self.event_id = event_id
        self.date = date
        self.time = time

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if self.log_id is None:
                cursor.execute('''
                INSERT INTO Access_Log 
                (employee_id, access_point_id, event_id, date, time)
                VALUES (?, ?, ?, ?, ?)
                ''', (self.employee_id, self.access_point_id, 
                     self.event_id, self.date, self.time))
                self.log_id = cursor.lastrowid
            else:
                cursor.execute('''
                UPDATE Access_Log SET
                    employee_id = ?,
                    access_point_id = ?,
                    event_id = ?,
                    date = ?,
                    time = ?
                WHERE log_id = ?
                ''', (self.employee_id, self.access_point_id,
                     self.event_id, self.date, self.time, self.log_id))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при сохранении записи доступа: {e}")
            raise
        finally:
            conn.close()

    def delete(self):
        """Удаляет запись из журнала доступа"""
        if self.log_id is not None:
            conn = get_connection()
            try:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Access_Log WHERE log_id = ?', (self.log_id,))
                conn.commit()
            except Exception as e:
                print(f"Ошибка при удалении записи: {e}")
                raise
            finally:
                conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Access_Log')
            return [Access_Log(*row) for row in cursor.fetchall()]
        finally:
            conn.close()

    @staticmethod
    def get_by_id(log_id):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Access_Log WHERE log_id = ?', (log_id,))
            row = cursor.fetchone()
            return Access_Log(*row) if row else None
        finally:
            conn.close()