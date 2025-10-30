class Task: 
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task added: {description}")

    def list_task(self):
        if not self.tasks:
            print("No tasks pending.")
        else:
            for task in self.tasks:
                print(task)

    def complete_task(self, id):
        task_id = int(id)  # Convertir a entero
        for task in self.tasks:
            if task.id == task_id:  # ✅ Usar task_id, no id
                task.completed = True
                print(f"Task #{task_id} marked as completed.")
                return         
        print(f"Task #{task_id} not found.")
        
    def delete_task(self, id):
        task_id = int(id)  # Convertir a entero
        for task in self.tasks:
            if task.id == task_id:  # ✅ Usar task_id, no id
                self.tasks.remove(task)
                print(f"Task #{task_id} deleted.")
                return  # ✅ Agregar return para salir del bucle
        print(f"Task #{task_id} not found.")  # ✅ Mensaje si no se encuentra