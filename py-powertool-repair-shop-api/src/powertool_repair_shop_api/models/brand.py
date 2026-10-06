from ..config.connection import get_connection

class BrandModel:
    
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT BrandID, BrandName FROM Brand')
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
