# worker.py
from db_connection import get_connection
from validate import validate_foreign_key
import psycopg


def list_workers():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "Worker"')
    tasks = cursor.fetchall()  # Збереження результату
    conn.close()
    return tasks


def add_worker(full_name, experience, salary, specialization_id):
    """
    Додає нового працівника після перевірки валідності зовнішнього ключа.
    """
    # Перевірка валідності зовнішнього ключа SpecID
    if not validate_foreign_key("Specialization", "SpecID", specialization_id):
        print(f"Error: Specialization with ID {specialization_id} does not exist.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cursor:
            # Додавання нового працівника
            cursor.execute(
                '''
                INSERT INTO "Worker" ("FullName", "ExperienceM", "Salary", "SpecID")
                VALUES (%s, %s, %s, %s)
                ''',
                (full_name, experience, salary, specialization_id)
            )
            conn.commit()
            print("Worker added successfully.")
    finally:
        conn.close()


def delete_worker(worker_id):
    try:
        conn = get_connection()
        if not conn:
            return
        with conn.cursor() as cursor:
            # Перевіряємо, чи є записи у таблиці Task
            cursor.execute('SELECT 1 FROM "Task" WHERE "WorkerID" = %s LIMIT 1', (worker_id,))
            if cursor.fetchone():
                print("Cannot delete worker: there are tasks associated with this worker.")
                return

            # Перевіряємо, чи є записи у таблиці Project/Worker
            cursor.execute('SELECT 1 FROM "Project/Worker" WHERE "WorkerID" = %s LIMIT 1', (worker_id,))
            if cursor.fetchone():
                print("Cannot delete worker: there are projects associated with this worker.")
                return

            # Видаляємо працівника
            cursor.execute('DELETE FROM "Worker" WHERE "WorkerID" = %s', (worker_id,))
            conn.commit()
            print("Worker deleted successfully.")
    except psycopg.DatabaseError as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def update_worker(worker_id, full_name=None, experience=None, salary=None, spec_id=None):
    conn = get_connection()
    cursor = conn.cursor()
    if full_name:
        cursor.execute('UPDATE "Worker" SET "FullName" = %s WHERE "WorkerID" = %s', (full_name, worker_id))
    if experience:
        cursor.execute('UPDATE "Worker" SET "ExperienceM" = %s WHERE "WorkerID" = %s', (experience, worker_id))
    if salary:
        cursor.execute('UPDATE "Worker" SET "Salary" = %s WHERE "WorkerID" = %s', (salary, worker_id))
    if spec_id:
        cursor.execute('UPDATE "Worker" SET "SpecID" = %s WHERE "WorkerID" = %s', (spec_id, worker_id))
    conn.commit()
    conn.close()
