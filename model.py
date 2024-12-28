from project import list_projects, add_project, delete_project, update_project
from worker import list_workers, add_worker, delete_worker, update_worker
from specialization import list_specializations, add_specialization, delete_specialization, update_specialization
from task import list_tasks, add_task, delete_task, update_task
from project_worker import list_project_workers, add_project_worker, delete_project_worker
from randomadd import generate_tasks, generate_projects, generate_specializations, generate_workers

from filter_project import filter_project
from filter_specialization import filter_specialization
from filter_worker import filter_worker
from filter_task import filter_task
from filter_project_worker import filter_project_worker

from db_connection import get_connection

class Model:

    def __init__(self):
        self.create_specialization_table()
        self.create_project_table()
        self.create_worker_table()
        self.create_task_table()
        self.create_employee_project_table()

        # Project-related methods

    def create_specialization_table(self):
        """Створює таблицю Specialization."""
        conn = get_connection()
        if not conn:
            return
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS public."Specialization" (
                        "SpecID" SERIAL PRIMARY KEY,
                        "SpecName" VARCHAR(255) NOT NULL,
                        "NumOfWorkers" INT NOT NULL
                    );
                """)
                conn.commit()
                print("Specialization table created.")
        finally:
            conn.close()

    def create_project_table(self):
        """Створює таблицю Project."""
        conn = get_connection()
        if not conn:
            return
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS public."Project" (
                        "ProjectID" SERIAL PRIMARY KEY,
                        "ProjectTitle" VARCHAR(255) NOT NULL
                    );
                """)
                conn.commit()
                print("Project table created.")
        finally:
            conn.close()

    def create_worker_table(self):
        """Створює таблицю Worker."""
        conn = get_connection()
        if not conn:
            return
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS public."Worker" (
                        "WorkerID" SERIAL PRIMARY KEY,
                        "FullName" VARCHAR(255) NOT NULL,
                        "ExperienceM" INT NOT NULL,
                        "Salary" INT NOT NULL,
                        "SpecID" INT NOT NULL,
                        CONSTRAINT "WorkerFkey" FOREIGN KEY ("SpecID")
                            REFERENCES public."Specialization" ("SpecID")
                            ON DELETE CASCADE
                    );
                """)
                conn.commit()
                print("Worker table created.")
        finally:
            conn.close()

    def create_task_table(self):
        """Створює таблицю Task."""
        conn = get_connection()
        if not conn:
            return
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS public."Task" (
                        "TaskID" SERIAL PRIMARY KEY,
                        "TaskTitle" VARCHAR(255) NOT NULL,
                        "Deadline" DATE NOT NULL,
                        "Status" VARCHAR(50) NOT NULL,
                        "WorkerID" INT NOT NULL,
                        "ProjectID" INT NOT NULL,
                        CONSTRAINT "TaskWorkerFkey" FOREIGN KEY ("WorkerID")
                            REFERENCES public."Worker" ("WorkerID")
                            ON DELETE CASCADE,
                        CONSTRAINT "TaskProjectFkey" FOREIGN KEY ("ProjectID")
                            REFERENCES public."Project" ("ProjectID")
                            ON DELETE CASCADE
                    );
                """)
                conn.commit()
                print("Task table created.")
        finally:
            conn.close()

    def create_employee_project_table(self):
        """Створює таблицю EmployeeProject."""
        conn = get_connection()
        if not conn:
            return
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS public."EmployeeProject" (
                        "EmployeeProjectID" SERIAL PRIMARY KEY,
                        "WorkerID" INT NOT NULL,
                        "ProjectID" INT NOT NULL,
                        CONSTRAINT "EmployeeProjectWorkerFkey" FOREIGN KEY ("WorkerID")
                            REFERENCES public."Worker" ("WorkerID")
                            ON DELETE CASCADE,
                        CONSTRAINT "EmployeeProjectProjectFkey" FOREIGN KEY ("ProjectID")
                            REFERENCES public."Project" ("ProjectID")
                            ON DELETE CASCADE
                    );
                """)
                conn.commit()
                print("EmployeeProject table created.")
        finally:
            conn.close()


    def list_projects(self):
        return list_projects()

    def add_project(self, title):
        add_project(title)

    def update_project(self, project_id, new_title):
        update_project(project_id, new_title)

    def delete_project(self, project_id):
        delete_project(project_id)

    def filter_project(self):
        return filter_project()

    def generate_projects(self, num):
        generate_projects(num)

        # Worker-related methods

    def list_workers(self):
        return list_workers()

    def add_worker(self, full_name, experience, salary, spec_id):
        add_worker(full_name, experience, salary, spec_id)

    def update_worker(self, worker_id, full_name=None, experience=None, salary=None, spec_id=None):
        update_worker(worker_id, full_name, experience, salary, spec_id)

    def delete_worker(self, worker_id):
        delete_worker(worker_id)

    def filter_worker(self):
        return filter_worker()

    def generate_workers(self, num):
        generate_workers(num)

        # Specialization-related methods

    def list_specializations(self):
        return list_specializations()

    def add_specialization(self, name, num_of_workers):
        add_specialization(name, num_of_workers)

    def update_specialization(self, spec_id, name=None, num_of_workers=None):
        update_specialization(spec_id, name, num_of_workers)

    def delete_specialization(self, spec_id):
        delete_specialization(spec_id)

    def filter_specialization(self):
        return filter_specialization()

    def generate_specializations(self, num):
        generate_specializations(num)

        # Task-related methods

    def list_tasks(self):
        return list_tasks()

    def add_task(self, title, deadline, status, worker_id, project_id):
        add_task(title, deadline, status, worker_id, project_id)

    def update_task(self, task_id, title=None, deadline=None, status=None, worker_id=None, project_id=None):
        update_task(task_id, title, deadline, status, worker_id, project_id)

    def delete_task(self, task_id):
        delete_task(task_id)

    def filter_task(self):
        return filter_task()

    def generate_tasks(self, num):
        generate_tasks(num)

        # ProjectWorker-related methods

    def list_project_workers(self):
        return list_project_workers()

    def add_project_worker(self, project_id, worker_id):
        add_project_worker(project_id, worker_id)

    def delete_project_worker(self, project_id, worker_id):
        delete_project_worker(project_id, worker_id)

    def filter_project_worker(self):
        return filter_project_worker()

