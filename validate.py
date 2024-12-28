from db_connection import get_connection
import psycopg

def validate_foreign_key(table_name, column_name, value):
    """
    Перевіряє, чи існує значення у вказаній таблиці та колонці.
    """
    conn = get_connection()
    if not conn:
        return False
    try:
        with conn.cursor() as cursor:
            query = f'SELECT COUNT(*) FROM "{table_name}" WHERE "{column_name}" = %s'
            cursor.execute(query, (value,))
            count = cursor.fetchone()[0]
            return count > 0
    finally:
        conn.close()