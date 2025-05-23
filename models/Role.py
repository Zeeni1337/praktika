from database.db_baaza_dannih import get_connection

class Role:
    def __init__(self, role_id=None, role_name=None):
        self.role_id = role_id
        self.role_name = role_name

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if self.role_id is None:
                cursor.execute('''
                INSERT INTO Role 
                (role_name)
                VALUES (?)
                ''', (self.role_name,))
                self.role_id = cursor.lastrowid
            else:
                cursor.execute('''
                UPDATE Role SET
                    role_name = ?
                WHERE role_id = ?
                ''', (self.role_name, self.role_id))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при сохранении роли: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Role')
            return [Role(*row) for row in cursor.fetchall()]
        finally:
            conn.close()