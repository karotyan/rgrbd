# manage_specialization.py
from db_connection import get_connection
import psycopg


def list_specializations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "Specialization"')
    specializations = cursor.fetchall()
    conn.close()
    return specializations

def add_specialization(name, num_of_workers):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO "Specialization" ("SpecName", "NumOfWorkers") VALUES (%s, %s)',
        (name, num_of_workers)
    )
    conn.commit()
    conn.close()

def delete_specialization(spec_id):
    try:
        conn = get_connection()
        if not conn:
            return
        with conn.cursor() as cursor:
            # Перевіряємо, чи є записи у таблиці Worker
            cursor.execute('SELECT 1 FROM "Worker" WHERE "SpecID" = %s LIMIT 1', (spec_id,))
            if cursor.fetchone():
                print("Cannot delete specialization: there are workers associated with this specialization.")
                return

            # Видаляємо спеціалізацію
            cursor.execute('DELETE FROM "Specialization" WHERE "SpecID" = %s', (spec_id,))
            conn.commit()
            print("Specialization deleted successfully.")
    except psycopg.DatabaseError as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def update_specialization(spec_id, name=None, num_of_workers=None):
    conn = get_connection()
    cursor = conn.cursor()
    if name:
        cursor.execute('UPDATE "Specialization" SET "SpecName" = %s WHERE "SpecID" = %s', (name, spec_id))
    if num_of_workers is not None:
        cursor.execute('UPDATE "Specialization" SET "NumOfWorkers" = %s WHERE "SpecID" = %s', (num_of_workers, spec_id))
    conn.commit()
    conn.close()

