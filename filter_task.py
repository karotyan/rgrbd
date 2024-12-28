import psycopg
from db_connection import get_connection
from datetime import datetime


def filter_task_by_title_or_deadline_or_status(title=None, deadline_start=None, deadline_end=None, status=None):
    """Фільтрація завдань за назвою, датами або статусом."""
    conn = get_connection()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            query = 'SELECT * FROM "Task" WHERE 1=1'
            params = []

            if title:
                query += ' AND "TaskTitle" LIKE %s'
                params.append(f'%{title}%')
            if deadline_start and deadline_end:
                query += ' AND "Deadline" BETWEEN %s AND %s'
                params.append(deadline_start)
                params.append(deadline_end)
            elif deadline_start:
                query += ' AND "Deadline" >= %s'
                params.append(deadline_start)
            elif deadline_end:
                query += ' AND "Deadline" <= %s'
                params.append(deadline_end)
            if status:
                query += ' AND "Status" LIKE %s'
                params.append(f'%{status}%')

            cursor.execute(query, params)
            results = cursor.fetchall()

            print(f"\n=== Search Results for Task ===")
            if results:
                for row in results:
                    print(row)
            else:
                print("No tasks found with the given filters.")

    finally:
        conn.close()


def prompt_for_task_filters():
    """Промпт для отримання фільтрів від користувача для таблиці Task."""
    print("\n=== Task Filtering ===")

    title = input("Enter task title to search (or leave blank to skip): ")

    # Перевірка дат на коректність формату
    while True:
        deadline_start = input("Enter start deadline (YYYY-MM-DD) to search (or leave blank to skip): ")
        if not deadline_start or validate_date(deadline_start):
            break
        print("Invalid start date format. Please enter a valid date (YYYY-MM-DD).")

    while True:
        deadline_end = input("Enter end deadline (YYYY-MM-DD) to search (or leave blank to skip): ")
        if not deadline_end or validate_date(deadline_end):
            break
        print("Invalid end date format. Please enter a valid date (YYYY-MM-DD).")

    status = input("Enter task status to search (or leave blank to skip): ")

    return title, deadline_start, deadline_end, status


def validate_date(date_string):
    """Перевірка формату дати (YYYY-MM-DD)."""
    try:
        if date_string:
            datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def filter_task():
    print("\n=== Filter Tasks ===")
    title, deadline_start, deadline_end, status = prompt_for_task_filters()

    # Перетворення дат у формат datetime, якщо вони є
    if deadline_start:
        deadline_start = datetime.strptime(deadline_start, "%Y-%m-%d").date()
    if deadline_end:
        deadline_end = datetime.strptime(deadline_end, "%Y-%m-%d").date()

    if title or deadline_start or status:
        filter_task_by_title_or_deadline_or_status(title, deadline_start, deadline_end, status)
    else:
        print("No valid filters provided. Exiting.")