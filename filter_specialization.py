import psycopg
from db_connection import get_connection


def filter_specialization_by_name_or_num_of_workers(name=None, num_of_workers=None):
    """Фільтрація спеціалізацій за назвою або кількістю працівників."""
    conn = get_connection()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            query = 'SELECT * FROM "Specialization" WHERE 1=1'
            params = []

            if name:
                query += ' AND "SpecName" LIKE %s'
                params.append(f'%{name}%')
            if num_of_workers:
                query += ' AND "NumOfWorkers" = %s'
                params.append(num_of_workers)

            cursor.execute(query, params)
            results = cursor.fetchall()

            print(f"\n=== Search Results for Specialization ===")
            if results:
                for row in results:
                    print(row)
            else:
                print("No specializations found with the given filters.")

    finally:
        conn.close()


def prompt_for_specialization_filters():
    """Промпт для отримання фільтрів від користувача для таблиці Specialization."""
    print("\n=== Specialization Filtering ===")

    name = input("Enter specialization name to search (or leave blank to skip): ")
    num_of_workers = input("Enter number of workers to search (or leave blank to skip): ")

    # Якщо користувач ввів кількість працівників, перевіримо, чи це число
    if num_of_workers:
        try:
            num_of_workers = int(num_of_workers)
        except ValueError:
            print("Invalid number of workers. Please enter a valid number.")
            return None
    else:
        num_of_workers = None

    return name, num_of_workers

def filter_specialization():
    print("\n=== Filter Specializations ===")
    name, num_of_workers = prompt_for_specialization_filters()

    if name is not None or num_of_workers is not None:
        filter_specialization_by_name_or_num_of_workers(name, num_of_workers)
    else:
        print("No valid filters provided. Exiting.")