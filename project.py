# manage_project.py
from db_connection import get_connection
import psycopg


def list_projects():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM "Project"')
    projects = cursor.fetchall()
    conn.close()
    return projects

def add_project(title):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO "Project" ("ProjectTitle") VALUES (%s)', (title,))
    conn.commit()
    conn.close()

def delete_project(project_id):
    try:
        conn = get_connection()
        if not conn:
            return
        with conn.cursor() as cursor:
            # Перевіряємо, чи є записи у дочірній таблиці Task
            cursor.execute('SELECT 1 FROM "Task" WHERE "ProjectID" = %s LIMIT 1', (project_id,))
            if cursor.fetchone():
                print("Cannot delete project: there are tasks associated with this project.")
                return

            # Перевіряємо, чи є записи у таблиці Project/Worker
            cursor.execute('SELECT 1 FROM "Project/Worker" WHERE "ProjectID" = %s LIMIT 1', (project_id,))
            if cursor.fetchone():
                print("Cannot delete project: there are workers associated with this project.")
                return

            # Видаляємо проект
            cursor.execute('DELETE FROM "Project" WHERE "ProjectID" = %s', (project_id,))
            conn.commit()
            print("Project deleted successfully.")
    except psycopg.DatabaseError as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def update_project(project_id, new_title):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE "Project" SET "ProjectTitle" = %s WHERE "ProjectID" = %s', (new_title, project_id))
    conn.commit()
    conn.close()
