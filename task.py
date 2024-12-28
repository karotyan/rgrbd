# task.py
from db_connection import get_connection
from validate import validate_foreign_key
import psycopg


def list_tasks():
    conn = get_connection()
    if not conn:
        return []
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "Task"')
    tasks = cursor.fetchall()  # Збереження результату
    conn.close()
    return tasks


def add_task(title, deadline, status, worker_id, project_id):
    """
    Додає нове завдання після перевірки валідності зовнішніх ключів.
    """
    if not validate_foreign_key("Worker", "WorkerID", worker_id):
        print(f"Error: Worker with ID {worker_id} does not exist.")
        return

    if not validate_foreign_key("Project", "ProjectID", project_id):
        print(f"Error: Project with ID {project_id} does not exist.")
        return

    conn = get_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO "Task" ("TaskTitle", "Deadline", "Status", "WorkerID", "ProjectID") VALUES (%s, %s, %s, %s, %s)',
                (title, deadline, status, worker_id, project_id)
            )
            conn.commit()
            print("Task added successfully.")
    finally:
        conn.close()


def update_task(task_id, title, deadline, status, worker_id, project_id):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE "Task" SET "TaskTitle" = %s, "Deadline" = %s, "Status" = %s, "WorkerID" = %s, "ProjectID" = %s WHERE "TaskID" = %s',
        (title, deadline, status, worker_id, project_id, task_id)
    )
    conn.commit()
    print("Task updated.")
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    cursor.execute('DELETE FROM "Task" WHERE "TaskID" = %s', (task_id,))
    conn.commit()
    print("Task deleted.")
    conn.close()
    
def update_task(task_id, title=None, deadline=None, status=None, worker_id=None, project_id=None):
    conn = get_connection()
    cursor = conn.cursor()
    if title:
        cursor.execute('UPDATE "Task" SET "TaskTitle" = %s WHERE "TaskID" = %s', (title, task_id))
    if deadline:
        cursor.execute('UPDATE "Task" SET "Deadline" = %s WHERE "TaskID" = %s', (deadline, task_id))
    if status:
        cursor.execute('UPDATE "Task" SET "Status" = %s WHERE "TaskID" = %s', (status, task_id))
    if worker_id:
        cursor.execute('UPDATE "Task" SET "WorkerID" = %s WHERE "TaskID" = %s', (worker_id, task_id))
    if project_id:
        cursor.execute('UPDATE "Task" SET "ProjectID" = %s WHERE "TaskID" = %s', (project_id, task_id))
    conn.commit()
    conn.close()


