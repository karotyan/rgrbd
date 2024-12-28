import psycopg
from db_connection import get_connection


def filter_worker_by_name_or_experience_or_salary(name=None, experience=None, salary=None):
    """Фільтрація працівників за ім'ям, досвідом або зарплатою."""
    conn = get_connection()
    if not conn:
        return

    try:
        with conn.cursor() as cursor:
            query = 'SELECT * FROM "Worker" WHERE 1=1'
            params = []

            if name:
                query += ' AND "FullName" LIKE %s'
                params.append(f'%{name}%')
            if experience:
                query += ' AND "ExperienceM" = %s'
                params.append(experience)
            if salary:
                query += ' AND "Salary" = %s'
                params.append(salary)

            cursor.execute(query, params)
            results = cursor.fetchall()

            print(f"\n=== Search Results for Worker ===")
            if results:
                for row in results:
                    print(row)
            else:
                print("No workers found with the given filters.")

    finally:
        conn.close()


def prompt_for_worker_filters():
    """Промпт для отримання фільтрів від користувача для таблиці Worker."""
    print("\n=== Worker Filtering ===")

    name = input("Enter worker name to search (or leave blank to skip): ")
    experience = input("Enter years of experience to search (or leave blank to skip): ")
    salary = input("Enter months to search (or leave blank to skip): ")

    # Якщо користувач ввів досвід, перевіримо, чи це число
    if experience:
        try:
            experience = int(experience)
        except ValueError:
            print("Invalid months of experience. Please enter a valid number.")
            return None
    else:
        experience = None

    # Якщо користувач ввів зарплату, перевіримо, чи це число
    if salary:
        try:
            salary = int(salary)
        except ValueError:
            print("Invalid salary. Please enter a valid number.")
            return None
    else:
        salary = None

    return name, experience, salary



        
def filter_worker():
    print("\n=== Filter Workers ===")
    name, experience, salary = prompt_for_worker_filters()

    if name is not None or experience is not None or salary is not None:
        filter_worker_by_name_or_experience_or_salary(name, experience, salary)
    else:
        print("No valid filters provided. Exiting.")
