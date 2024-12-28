from model import Model
from view import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()  # Створення об'єкта представлення

    def project_menu(self):
        while True:
            print("\n=== Project Menu ===")
            print("1. View Projects")
            print("2. Add Project")
            print("3. Update Project")
            print("4. Delete Project")
            print("5. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                projects = self.model.list_projects()
                self.view.show_projects(projects)
            elif choice == "2":
                title = self.view.get_project_title()
                self.model.add_project(title)
                self.view.show_message("Project added successfully.")
            elif choice == "3":
                project_id = self.view.get_project_id()
                new_title = self.view.get_new_project_title()
                self.model.update_project(project_id, new_title)
                self.view.show_message("Project updated successfully.")
            elif choice == "4":
                project_id = self.view.get_project_id()
                self.model.delete_project(project_id)
                self.view.show_message("Project deleted successfully.")
            elif choice == "5":
                break
            else:
                print("Invalid option. Try again.")

    def worker_menu(self):
        while True:
            print("\n=== Worker Menu ===")
            print("1. View Workers")
            print("2. Add Worker")
            print("3. Update Worker")
            print("4. Delete Worker")
            print("5. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                workers = self.model.list_workers()
                self.view.show_worker_list(workers)
            elif choice == "2":
                full_name, experience, salary, spec_id = self.view.get_worker_details()
                self.model.add_worker(full_name, experience, salary, spec_id)
                self.view.show_message("Worker added successfully.")
            elif choice == "3":
                worker_id = self.view.get_worker_id()
                full_name, experience, salary, spec_id = self.view.get_worker_update_details()
                self.model.update_worker(worker_id, full_name or None, 
                                         int(experience) if experience else None, 
                                         int(salary) if salary else None, 
                                         int(spec_id) if spec_id else None)
                self.view.show_message("Worker updated successfully.")
            elif choice == "4":
                worker_id = self.view.get_worker_id()
                self.model.delete_worker(worker_id)
                self.view.show_message("Worker deleted successfully.")
            elif choice == "5":
                break
            else:
                print("Invalid option. Try again.")

    def specialization_menu(self):
        while True:
            print("\n=== Specialization Menu ===")
            print("1. View Specializations")
            print("2. Add Specialization")
            print("3. Update Specialization")
            print("4. Delete Specialization")
            print("5. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                specializations = self.model.list_specializations()
                self.view.show_specializations(specializations)
            elif choice == "2":
                name, num_of_workers = self.view.get_specialization_details()
                self.model.add_specialization(name, num_of_workers)
                self.view.show_message("Specialization added successfully.")
            elif choice == "3":
                spec_id = self.view.get_specialization_id()
                name, num_of_workers = self.view.get_specialization_update_details()
                self.model.update_specialization(spec_id, name or None, 
                                                 int(num_of_workers) if num_of_workers else None)
                self.view.show_message("Specialization updated successfully.")
            elif choice == "4":
                spec_id = self.view.get_specialization_id()
                self.model.delete_specialization(spec_id)
                self.view.show_message("Specialization deleted successfully.")
            elif choice == "5":
                break
            else:
                print("Invalid option. Try again.")

    def task_menu(self):
        while True:
            print("\n=== Task Menu ===")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                tasks = self.model.list_tasks()
                self.view.show_tasks(tasks)
            elif choice == "2":
                title, deadline, status, worker_id, project_id = self.view.get_task_details()
                self.model.add_task(title, deadline, status, worker_id, project_id)
                self.view.show_message("Task added successfully.")
            elif choice == "3":
                task_id = self.view.get_task_id()
                title, deadline, status, worker_id, project_id = self.view.get_task_update_details()
                self.model.update_task(task_id, title or None, deadline or None, 
                                        status or None, 
                                        int(worker_id) if worker_id else None, 
                                        int(project_id) if project_id else None)
                self.view.show_message("Task updated successfully.")
            elif choice == "4":
                task_id = self.view.get_task_id()
                self.model.delete_task(task_id)
                self.view.show_message("Task deleted successfully.")
            elif choice == "5":
                break
            else:
                print("Invalid option. Try again.")

    def project_worker_menu(self):
        while True:
            print("\n=== Project/Worker Menu ===")
            print("1. View Project/Worker Relations")
            print("2. Add Project/Worker Relation")
            print("3. Delete Project/Worker Relation")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                relations = self.model.list_project_workers()
                self.view.show_project_worker_relations(relations)
            elif choice == "2":
                project_id, worker_id = self.view.get_project_worker_details()
                self.model.add_project_worker(project_id, worker_id)
                self.view.show_message("Relation added successfully.")
            elif choice == "3":
                project_id, worker_id = self.view.get_project_worker_details()
                self.model.delete_project_worker(project_id, worker_id)
                self.view.show_message("Relation deleted successfully.")
            elif choice == "4":
                break
            else:
                print("Invalid option. Try again.")

    def randomadd_menu(self):
        while True:
            print("\n=== Add new data Menu ===")
            print("1. Add Projects")
            print("2. Add Specializations")
            print("3. Add Workers")
            print("4. Add Tasks")
            print("5. Back to Main Menu")

            choice = input("Choose an option: ")
            if choice == "1":
                num = self.view.get_number_of_records()
                self.model.generate_projects(num)
                self.view.show_message("Projects added successfully.")
            elif choice == "2":
                num = self.view.get_number_of_records()
                self.model.generate_specializations(num)
                self.view.show_message("Specializations added successfully.")
            elif choice == "3":
                num = self.view.get_number_of_records()
                self.model.generate_workers(num)
                self.view.show_message("Workers added successfully.")
            elif choice == "4":
                num = self.view.get_number_of_records()
                self.model.generate_tasks(num)
                self.view.show_message("Tasks added successfully.")
            elif choice == "5":
                break
            else:
                print("Invalid option. Try again.")

    def filter_menu(self):
        while True:
            print("\n=== Filter table ===")
            print("1. Filter Project")
            print("2. Filter Specialization")
            print("3. Filter Worker")
            print("4. Filter Task")
            print("5. Filter Project/Worker")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.model.filter_project()
            elif choice == "2":
                self.model.filter_specialization()
            elif choice == "3":
                self.model.filter_worker()
            elif choice == "4":
                self.model.filter_task()
            elif choice == "5":
                self.model.filter_project_worker()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

    def main_menu(self):
        while True:
            print("\n=== Main Menu ===")
            print("1. Manage Projects")
            print("2. Manage Workers")
            print("3. Manage Specializations")
            print("4. Manage Tasks")
            print("5. Manage Project/Worker Relations")
            print("6. Exit")
            print("7. Generate Random Data")
            print("8. Get filter data")

            choice = input("Choose an option: ")

            if choice == "1":
                self.project_menu()
            elif choice == "2":
                self.worker_menu()
            elif choice == "3":
                self.specialization_menu()
            elif choice == "4":
                self.task_menu()
            elif choice == "5":
                self.project_worker_menu()
            elif choice == "6":
                print("Goodbye!")
                break
            elif choice == "7":
                self.randomadd_menu()
            elif choice == "8":
                self.filter_menu()
            else:
                print("Invalid option. Try again.")