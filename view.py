class View:

    def show_projects(self, projects):
        print("\n=== Projects ===")
        for project in projects:
            print(f"ID: {project[0]}, Title: {project[1]}")

    def get_project_title(self):
        return input("Enter project title: ")

    def get_new_project_title(self):
        return input("Enter new project title: ")

    def get_project_id(self):
        return int(input("Enter project ID: "))

    def show_worker_list(self, workers):
        print("\n=== Workers ===")
        for worker in workers:
            print(f"ID: {worker[0]}, Name: {worker[4]}, Experience (months): {worker[1]}, Salary: {worker[2]}, Specialization ID: {worker[3]}")

    def get_worker_details(self):
        full_name = input("Enter full name: ")
        experience = int(input("Enter experience in months: "))
        salary = int(input("Enter salary: "))
        spec_id = int(input("Enter specialization ID: "))
        return full_name, experience, salary, spec_id

    def get_worker_id(self):
        return int(input("Enter worker ID: "))

    def get_worker_update_details(self):
        full_name = input("Enter new full name (leave blank to skip): ")
        experience = input("Enter new experience in months (leave blank to skip): ")
        salary = input("Enter new salary (leave blank to skip): ")
        spec_id = input("Enter new specialization ID (leave blank to skip): ")
        return full_name, experience, salary, spec_id

    def show_specializations(self, specializations):
        print("\n=== Specializations ===")
        for spec in specializations:
            print(f"ID: {spec[0]}, Name: {spec[1]}, Number of Workers: {spec[2]}")

    def get_specialization_details(self):
        name = input("Enter specialization name: ")
        num_of_workers = int(input("Enter number of workers: "))
        return name, num_of_workers

    def get_specialization_id(self):
        return int(input("Enter specialization ID: "))

    def get_specialization_update_details(self):
        name = input("Enter new name (leave blank to skip): ")
        num_of_workers = input("Enter new number of workers (leave blank to skip): ")
        return name, num_of_workers

    def show_tasks(self, tasks):
        print("\n=== Tasks ===")
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Deadline: {task[2]}, Status: {task[3]}, Worker ID: {task[4]}, Project ID: {task[5]}")

    def get_task_details(self):
        title = input("Enter task title: ")
        deadline = input("Enter deadline (YYYY-MM-DD): ")
        status = input("Enter status: ")
        worker_id = int(input("Enter worker ID: "))
        project_id = int(input("Enter project ID: "))
        return title, deadline, status, worker_id, project_id

    def get_task_id(self):
        id = input("Enter task ID: ")
        return id

    def get_task_update_details(self):
        title = input("Enter new task title (leave blank to skip): ")
        deadline = input("Enter new deadline (leave blank to skip): ")
        status = input("Enter new status (leave blank to skip): ")
        worker_id = input("Enter new worker ID (leave blank to skip): ")
        project_id = input("Enter new project ID (leave blank to skip): ")
        return title, deadline, status, worker_id, project_id

    def show_project_worker_relations(self, relations):
        print("\n=== Project/Worker Relations ===")
        for relation in relations:
            print(f"Project ID: {relation[0]}, Worker ID: {relation[1]}")

    def get_project_worker_details(self):
        project_id = int(input("Enter project ID: "))
        worker_id = int(input("Enter worker ID: "))
        return project_id, worker_id

    def show_message(self, message):
        print(message)

    def get_number_of_records(self):
        return int(input("Enter the number of records to add: "))