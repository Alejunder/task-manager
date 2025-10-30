from task_manager import TaskManager

def print_menu():
       print("Gestor de Tareas Inteligente")
       print("1. Agregar Tarea")
       print("2. Listar Tareas")
       print("3. Completar Tarea")
       print("4. Eliminar Tarea")
       print("5. Salir")

def main(): 
   
  manager = TaskManager()
   
  while True:  
    
       print_menu()
    
       choice = input ("Seleccione una opción: ")
    
       match choice:
         case "1":
            description = input("Descripción de la tarea: ") 
            manager.add_task(description)
            
         case "2":
            manager.list_task()
         case "3":
            id = input("ID de la tarea a completar: ")
            manager.complete_task(id)  
         case "4":
            id = input("ID de la tarea a eliminar: ")
            manager.delete_task(id)  
         case "5":
            print("Saliendo...")
            break
         case _:
            print("Opción no válida. Selecciona otra.")
             
if __name__ == "__main__":
    main()            