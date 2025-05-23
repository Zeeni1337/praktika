from database.db_baaza_dannih import get_connection

class Position:
    def __init__(self, position_id=None, position_name=None):
        self.position_id = position_id
        self.position_name = position_name

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if self.position_id is None:
                cursor.execute('''
                INSERT INTO Position 
                (position_name)
                VALUES (?)
                ''', (self.position_name,))
                self.position_id = cursor.lastrowid
            else:
                cursor.execute('''
                UPDATE Position SET
                    position_name = ?
                WHERE position_id = ?
                ''', (self.position_name, self.position_id))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при сохранении должности: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Position')
            return [Position(*row) for row in cursor.fetchall()]
        finally:
            conn.close()