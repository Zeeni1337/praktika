from database.db_baaza_dannih import get_connection

class Service:
    def __init__(self, service_id=None, service_name=None, description=None):
        self.service_id = service_id
        self.service_name = service_name
        self.description = description

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if self.service_id is None:
                cursor.execute('''
                INSERT INTO Service 
                (service_name, description)
                VALUES (?, ?)
                ''', (self.service_name, self.description))
                self.service_id = cursor.lastrowid
            else:
                cursor.execute('''
                UPDATE Service SET
                    service_name = ?,
                    description = ?
                WHERE service_id = ?
                ''', (self.service_name, self.description, self.service_id))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при сохранении услуги: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Service')
            return [Service(*row) for row in cursor.fetchall()]
        finally:
            conn.close()