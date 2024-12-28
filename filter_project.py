import psycopg
from db_connection import get_connection


def filter_project_by_name_or_id(name=None, project_id=None):
    """Фільтрація проектів за назвою або ID."""
    conn = get_connection()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            query = 'SELECT * FROM "Project" WHERE 1=1'
            params = []

            if name:
                query += ' AND "ProjectTitle" LIKE %s'
                params.append(f'%{name}%')
            if project_id:
                query += ' AND "ProjectID" = %s'
                params.append(project_id)

            cursor.execute(query, params)
            results = cursor.fetchall()

            print(f"\n=== Search Results for Project ===")
            if results:
                for row in results:
                    print(row)
            else:
                print("No projects found with the given filters.")

    finally:
        conn.close()
        
        
def prompt_for_project_filters():
    """Промпт для отримання фільтрів від користувача для таблиці Project."""
    print("\n=== Project Filtering ===")

    name = input("Enter project name to search (or leave blank to skip): ")
    project_id = input("Enter project ID to search (or leave blank to skip): ")

    # Якщо користувач ввів ID, перевіримо, чи це число
    if project_id:
        try:
            project_id = int(project_id)
        except ValueError:
            print("Invalid project ID. Please enter a valid number.")
            return None
    else:
        project_id = None

    return name, project_id


def filter_project():
    print("\n=== Filter Projects ===")
    name, project_id = prompt_for_project_filters()

    if name is not None or project_id is not None:
        filter_project_by_name_or_id(name, project_id)
    else:
        print("No valid filters provided. Exiting.")