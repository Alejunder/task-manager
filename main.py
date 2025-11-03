from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
       print("Gestor de Tareas Inteligente")
       print("1. Agregar Tarea")
       print("2. Agregar Tarea Compleja (con IA)")
       print("3. Listar Tareas")
       print("4. Completar Tarea")
       print("5. Eliminar Tarea")
       print("6. Salir")

def main(): 
   
  manager = TaskManager()
   
  while True:  
    
       print_menu()
       
       try:
            choice = input ("Seleccione una opción: ")
         
            match choice:
               case "1":
                  description = input("Descripción de la tarea: ") 
                  manager.add_task(description)
                  
               case "2":
                  description = input("Descripción de la tarea: ") 
                  subtasks = create_simple_tasks(description)   
                  for subtask in subtasks:
                      if not subtask.startswith("Error:"):
                         manager.add_task(subtask) 
                      else:
                         print(subtask)    
                         break
                  
               case "3":
                  manager.list_task()
               case "4":
                  id = int(input("ID de la tarea a completar: "))
                  manager.complete_task(id)  
               case "5":
                  id = input("ID de la tarea a eliminar: ")
                  manager.delete_task(id)  
               case "6":
                  print("Saliendo...")
                  break
               case _:
                  print("Opción no válida. Selecciona otra.")
       except ValueError:
            print("Opción no válida. Seleccionba otra.")    
             
if __name__ == "__main__":
    main()            