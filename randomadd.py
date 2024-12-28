from db_connection import get_connection
import psycopg

def generate_specializations(count):

    """Генерує спеціалізації з використанням SQL."""
    conn = get_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cursor:
            query = f"""
            INSERT INTO "Specialization" ("SpecName", "NumOfWorkers")
            SELECT
                substring(md5(random()::text) FROM 1 FOR 15), -- випадковий рядок
                floor(random() * 46 + 5)::int -- число від 5 до 50
            FROM generate_series(1, {count});
            """
            cursor.execute(query)
        conn.commit()
        print(f"{count} specializations added.")
    finally:
        conn.close()


def generate_projects(count):
    """Генерує проєкти з використанням SQL."""
    conn = get_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cursor:
            query = f"""
            INSERT INTO "Project" ("ProjectTitle")
            SELECT
                substring(md5(random()::text) FROM 1 FOR 20) -- випадковий рядок
            FROM generate_series(1, {count});
            """
            cursor.execute(query)
        conn.commit()
        print(f"{count} projects added.")
    finally:
        conn.close()


def generate_workers(count):
    """Генерує працівників з використанням SQL."""
    conn = get_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cursor:
            query = f"""
            INSERT INTO "Worker" ("FullName", "ExperienceM", "Salary", "SpecID")
            SELECT
                substring(md5(random()::text) FROM 1 FOR 15), -- випадкове ім'я
                floor(random() * 241)::int, -- досвід у місяцях (0-240)
                floor(random() * 4701 + 300)::int, -- зарплата (300-5000)
                (
                    SELECT "SpecID"
                    FROM "Specialization"
                    OFFSET floor(random() * (SELECT COUNT(*) FROM "Specialization"))::int
                    LIMIT 1
                ) -- випадковий SpecID
            FROM generate_series(1, {count});
            """
            cursor.execute(query)
        conn.commit()
        print(f"{count} workers added.")
    finally:
        conn.close()


def generate_tasks(count):
    """Генерує завдання з використанням SQL."""
    conn = get_connection()
    if not conn:
        return
    try:
        with conn.cursor() as cursor:
            query = f"""
            INSERT INTO "Task" ("TaskTitle", "Deadline", "Status", "WorkerID", "ProjectID")
            SELECT
                substring(md5(random()::text) FROM 1 FOR 20), -- випадковий заголовок завдання
                CURRENT_DATE + floor(random() * 365 + 1)::int, -- випадковий дедлайн
                (ARRAY['Pending', 'In Progress', 'Completed'])[floor(random() * 3 + 1)::int], -- випадковий статус
                (
                    SELECT "WorkerID"
                    FROM "Worker"
                    OFFSET floor(random() * (SELECT COUNT(*) FROM "Worker"))::int
                    LIMIT 1
                ), -- випадковий WorkerID
                (
                    SELECT "ProjectID"
                    FROM "Project"
                    OFFSET floor(random() * (SELECT COUNT(*) FROM "Project"))::int
                    LIMIT 1
                ) -- випадковий ProjectID
            FROM generate_series(1, {count});
            """
            cursor.execute(query)
        conn.commit()
        print(f"{count} tasks added.")
    finally:
        conn.close()