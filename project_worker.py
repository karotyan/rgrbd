# manage_project_worker.py
from db_connection import get_connection
from validate import validate_foreign_key
import psycopg

def list_project_workers():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "Project/Worker"')
    project_workers = cursor.fetchall()  # Збереження результату
    conn.close()
    return project_workers


def add_project_worker(project_id, worker_id):
    """
    Додає зв'язок між проектом і працівником після перевірки валідності зовнішніх ключів.
    """
    if not validate_foreign_key("Project", "ProjectID", project_id):
        print(f"Error: Project with ID {project_id} does not exist.")
        return

    if not validate_foreign_key("Worker", "WorkerID", worker_id):
        print(f"Error: Worker with ID {worker_id} does not exist.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO "ProjectWorker" ("ProjectID", "WorkerID") VALUES (%s, %s)',
                (project_id, worker_id)
            )
            conn.commit()
            print("Project-Worker relation added successfully.")
    finally:
        conn.close()


def delete_project_worker(project_id, worker_id):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM "Project/Worker" WHERE "ProjectID" = %s AND "WorkerID" = %s',
        (project_id, worker_id)
    )
    conn.commit()
    print("Project/Worker relation deleted.")
    conn.close()

