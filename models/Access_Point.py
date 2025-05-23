from database.db_baaza_dannih import get_connection

class Access_Point:
    def __init__(self, access_point_id=None, access_point_name=None, room=None):
        self.access_point_id = access_point_id
        self.access_point_name = access_point_name
        self.room = room

    def save(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            if self.access_point_id is None:
                cursor.execute('''
                INSERT INTO Access_Point 
                (access_point_name, room)
                VALUES (?, ?)
                ''', (self.access_point_name, self.room))
                self.access_point_id = cursor.lastrowid
            else:
                cursor.execute('''
                UPDATE Access_Point SET
                    access_point_name = ?,
                    room = ?
                WHERE access_point_id = ?
                ''', (self.access_point_name, self.room, self.access_point_id))
            conn.commit()
        except Exception as e:
            print(f"Ошибка при сохранении точки доступа: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def get_all():
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Access_Point')
            return [Access_Point(*row) for row in cursor.fetchall()]
        finally:
            conn.close()