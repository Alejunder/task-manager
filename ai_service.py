import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def create_simple_tasks(description):
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return ["Error: Google API key is not configured."]
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""Eres un asistente experto en gestión de tareas que ayuda a desglosar tareas complejas en subtareas simples y accionables.

Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables. 
        
Tarea: {description}

Formato de respuesta:
- Subtarea 1
- Subtarea 2
- Subtarea 3
- etc.

Responde solo con la lista de subtareas, una por línea, empezando cada línea con un guion (-)."""
        
        response = model.generate_content(prompt)
        
        content = response.text.strip()
        
        subtasks = []
        
        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        
        return subtasks if subtasks else ["Error: No se pudieron generar subtareas."]

    except Exception as e:
        return [f"Error: Unable to connect to the AI service. {str(e)}"]