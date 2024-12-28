import psycopg
from db_connection import get_connection


def filter_project_worker(project_id=None, worker_id=None):
    """Фільтрація записів між проектами та працівниками за проектом або працівником."""
    conn = get_connection()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            query = 'SELECT * FROM "Project/Worker" WHERE 1=1'
            params = []

            if project_id:
                query += ' AND "ProjectID" = %s'
                params.append(project_id)
            if worker_id:
                query += ' AND "WorkerID" = %s'
                params.append(worker_id)

            cursor.execute(query, params)
            results = cursor.fetchall()

            print(f"\n=== Search Results for Project/Worker ===")
            if results:
                for row in results:
                    print(row)
            else:
                print("No relations found with the given filters.")

    finally:
        conn.close()


def prompt_for_project_worker_filters():
    """Промпт для отримання фільтрів від користувача для таблиці Project/Worker."""
    print("\n=== Project/Worker Filtering ===")

    project_id = input("Enter project ID to search (or leave blank to skip): ")
    worker_id = input("Enter worker ID to search (or leave blank to skip): ")

    # Якщо користувач ввів project_id, перевіримо, чи це число
    if project_id:
        try:
            project_id = int(project_id)
        except ValueError:
            print("Invalid project ID. Please enter a valid number.")
            return None
    else:
        project_id = None

    # Якщо користувач ввів worker_id, перевіримо, чи це число
    if worker_id:
        try:
            worker_id = int(worker_id)
        except ValueError:
            print("Invalid worker ID. Please enter a valid number.")
            return None
    else:
        worker_id = None

    return project_id, worker_id


def filter_project_worker():
    print("\n=== Filter Project/Worker ===")
    project_id, worker_id = prompt_for_project_worker_filters()

    if project_id is not None or worker_id is not None:
        filter_project_worker(project_id, worker_id)
    else:
        print("No valid filters provided. Exiting.")

