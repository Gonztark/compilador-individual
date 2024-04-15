import tkinter as tk
from tkinter import filedialog
import customtkinter
from lexico import analizar_lexico, reset_lines
from sintactico import analizar_sintactico
from translate import translate_to_python, translate_ast
from optimizacion import optimize_ast
import io
import sys
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("green")  


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()




        self.title("Compilador Metal Gear")
        self.configure(fg_color='#2e2e2e')
        self.geometry("1250x750") 

        

        # Cargar la imagen de fondo
        #self.background_image = Image.open("background.png")  # Asegúrate de poner la ruta correcta aquí
        #self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Configurar un label como contenedor de la imagen de fondo
        #self.background_label = tk.Label(self, image=self.background_photo)
        #self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame para contener el cuadro de texto y los números de línea
        self.frame_texto = customtkinter.CTkFrame(self)
        self.frame_texto.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Cuadro de texto para los números de línea
        self.texto_lineas = tk.Text(self.frame_texto, width=4, height=24, state='disabled', takefocus=0, bd=0, background='lightgrey', font='TkFixedFont')
        self.texto_lineas.pack(side="left", fill="y")

        # Cuadro de texto para la entrada del usuario
        self.texto_entrada = customtkinter.CTkTextbox(self.frame_texto, width=380, height=300)
        self.texto_entrada.pack(side="right", fill="both", expand=True)
        self.texto_entrada.insert("1.0", "Introduce el código aquí o carga un archivo")
        self.texto_entrada.bind("<FocusIn>", self.on_focus_in)
        self.texto_entrada.bind("<KeyRelease>", self.actualizar_numeros_linea)



        # Mostrar resultado léxico
        self.label_resultado_lexico = customtkinter.CTkLabel(self, text="Tabla de Símbolos", font=("Arial", 18, "bold"))
        self.label_resultado_lexico.place(x=450, y=5)

        self.texto_resultado_lexico = customtkinter.CTkTextbox(self, width=380, height=250, state="disabled")
        self.texto_resultado_lexico.grid(row=0, column=1, padx=20, pady=(20,0))
        self.texto_resultado_lexico.place(x=450, y=35)


        # Mostrar resultado sintáctico
        self.label_resultado_lexico = customtkinter.CTkLabel(self, text="Errores", font=("Arial", 18, "bold"))
        self.label_resultado_lexico.place(x=20, y=440)

        self.texto_resultado_sintactico = customtkinter.CTkTextbox(self, width=400, height=250, state="disabled")
        self.texto_resultado_sintactico.place(x=20, y=470)


        # Mostrar representación intermedia
        self.label_resultado_intermedio = customtkinter.CTkLabel(self, text="Código Intermedio", font=("Arial", 18, "bold"))
        self.label_resultado_intermedio.place(x=450, y=440)

        self.texto_resultado_intermedio = customtkinter.CTkTextbox(self, width=380, height=250, state="disabled")
        self.texto_resultado_intermedio.place(x=450, y=470)

        # Mostrar código en python
        self.label_resultado_python = customtkinter.CTkLabel(self, text="Código en Python", font=("Arial", 18, "bold"))
        self.label_resultado_python.place(x=850, y=5)

        self.texto_resultado_python = customtkinter.CTkTextbox(self, width=380, height=250, state="disabled")
        self.texto_resultado_python.grid(row=0, column=1, padx=20, pady=(20,0))
        self.texto_resultado_python.place(x=850, y=35)

        # Consola
        self.label_resultado_consola = customtkinter.CTkLabel(self, text="Consola", font=("Arial", 18, "bold"))
        self.label_resultado_consola.place(x=850, y=440)

        self.texto_resultado_consola = customtkinter.CTkTextbox(self, width=380, height=250, state="disabled")
        self.texto_resultado_consola.grid(row=0, column=1, padx=20, pady=(20,0))
        self.texto_resultado_consola.place(x=850, y=470)

        # botones
        self.boton_analizar_lexico = customtkinter.CTkButton(self, text="Analizar Léxico", command=self.analizar_lexico)
        self.boton_analizar_lexico.place(x=570, y=320)

        self.boton_analizar_sintactico = customtkinter.CTkButton(self, text="Traducir el código", command=self.analizar_sintactico)
        self.boton_analizar_sintactico.place(x=570, y=370)


        self.boton_cargar = customtkinter.CTkButton(self, text="Cargar Archivo", command=self.cargar_archivo)
        self.boton_cargar.place(x=160, y=410)

        self.boton_ejecutar_codigo = customtkinter.CTkButton(self, text="Ejecutar", command=self.ejecutar_codigo)
        self.boton_ejecutar_codigo.place(x=970, y=300)

        #LABELSSSS
        #3


    def actualizar_numeros_linea(self, event=None):
        self.texto_lineas.configure(state='normal')
        self.texto_lineas.delete('1.0', 'end')

        numero_lineas = self.texto_entrada.get('1.0', 'end-1c').split('\n')
        for i in range(len(numero_lineas)):
            self.texto_lineas.insert('end', f'{i + 1}\n')

        self.texto_lineas.configure(state='disabled')

    def on_focus_in(self, event):
        default_text = "Introduce el código aquí o carga un archivo"
        if self.texto_entrada.get("1.0", "end-1c") == default_text:
            self.texto_entrada.delete("1.0", "end")

    def analizar_lexico(self):
        texto_usuario = self.texto_entrada.get("1.0", "end-1c")
        resultado = analizar_lexico(texto_usuario)
        reset_lines()

        self.texto_resultado_lexico.configure(state="normal")
        self.texto_resultado_lexico.delete("1.0", "end")
        self.texto_resultado_lexico.insert("1.0", resultado)
        self.texto_resultado_lexico.configure(state="disabled")

    def analizar_sintactico(self):
        texto_usuario = self.texto_entrada.get("1.0", "end-1c")
        resultado, ast, symbol_table, function_table = analizar_sintactico(texto_usuario)
        reset_lines()
        if not resultado.strip():
            resultado = "No se han detectado errores."
            print("AST:")
            print(ast)
            ast_formated = translate_ast(ast)

            self.texto_resultado_sintactico.configure(state="normal")
            self.texto_resultado_sintactico.delete("1.0", "end")
            self.texto_resultado_sintactico.insert("1.0", resultado)
            self.texto_resultado_sintactico.configure(state="disabled")
            

            self.texto_resultado_lexico.configure(state="normal")
            self.texto_resultado_lexico.delete("1.0", "end")
            self.texto_resultado_lexico.insert("1.0", "Variables:\n")

            for variable, data in symbol_table.items():
                self.texto_resultado_lexico.insert("end", f"{variable}:\n")
                self.texto_resultado_lexico.insert("end", f"  Tipo: {data['type']}\n")
                self.texto_resultado_lexico.insert("end", f"  Contenido: {data['value']}\n")
                self.texto_resultado_lexico.insert("end", "\n")

            self.texto_resultado_lexico.insert("end", "\nFunciones:\n")


            for function, data in function_table.items():
                self.texto_resultado_lexico.insert("end", f"{function}:\n")
                self.texto_resultado_lexico.insert("end", f"  Parámetros: {data['parameters']}\n")
                self.texto_resultado_lexico.insert("end", f"  Bloque:\n")
                for statement in data['block']:
                    self.texto_resultado_lexico.insert("end", f"    {statement['type']}\n")
                self.texto_resultado_lexico.insert("end", "\n")

            self.texto_resultado_lexico.configure(state="disabled")

            self.texto_resultado_intermedio.configure(state="normal")
            self.texto_resultado_intermedio.delete("1.0", "end")
            self.texto_resultado_intermedio.insert("1.0", ast_formated)
            self.texto_resultado_intermedio.configure(state="disabled")

            optimized_ast = optimize_ast(ast, symbol_table)
            print("OPTIMIZEDDD:")
            print(optimized_ast)
            python_code = translate_to_python(optimized_ast)

            self.texto_resultado_python.configure(state="normal")
            self.texto_resultado_python.delete("1.0", "end")
            self.texto_resultado_python.insert("1.0", python_code)
            self.texto_resultado_python.configure(state="disabled")

        else:
            ast = "Corrige los errores primero."
            self.texto_resultado_consola.configure(state="normal")
            self.texto_resultado_consola.delete("1.0", "end")
            self.texto_resultado_consola.insert("1.0", "")
            self.texto_resultado_consola.configure(state="disabled")
            self.texto_resultado_python.configure(state="normal")
            self.texto_resultado_python.delete("1.0", "end")
            self.texto_resultado_python.insert("1.0", "")
            self.texto_resultado_python.configure(state="disabled")

        self.texto_resultado_sintactico.configure(state="normal")
        self.texto_resultado_sintactico.delete("1.0", "end")
        self.texto_resultado_sintactico.insert("1.0", resultado)
        self.texto_resultado_sintactico.configure(state="disabled")

        self.texto_resultado_intermedio.configure(state="normal")
        self.texto_resultado_intermedio.delete("1.0", "end")
        self.texto_resultado_intermedio.insert("1.0", ast_formated)
        self.texto_resultado_intermedio.configure(state="disabled")
        



    def cargar_archivo(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            with open(filepath, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                self.texto_entrada.configure(state="normal")
                self.texto_entrada.delete("1.0", "end")
                self.texto_entrada.insert("1.0", contenido)
                self.texto_entrada.configure(state="normal")
                
    def custom_input(self, prompt):
        # Crear el cuadro de diálogo para la entrada del usuario
        dialog = customtkinter.CTkInputDialog(text=prompt, title="Entrada de usuario")
        x_position = 600 
        y_position = 300 
        dialog.geometry(f"+{x_position}+{y_position}")

        input_value = dialog.get_input()

        try:
            # Intentar convertir la entrada a un entero
            return int(input_value)
        except ValueError:
            # Devolver el valor original si la conversión falla
            return input_value



    def ejecutar_codigo(self):
        codigo = self.texto_resultado_python.get("1.0", "end-1c")
        
        # Redirigir stdout y stderr a la consola de la GUI
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = StdoutRedirector(self.texto_resultado_consola)
        sys.stderr = StdoutRedirector(self.texto_resultado_consola)
    
        try:
            exec(codigo, {'input': lambda prompt='': self.custom_input(prompt)})
        except Exception as e:
            print(str(e))  # Esto se mostrará en la consola de la GUI
        finally:
            # Restaurar stdout y stderr
            sys.stdout = old_stdout
            sys.stderr = old_stderr


class StdoutRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, string):
        self.widget.configure(state='normal')
        self.widget.insert('end', string)
        self.widget.configure(state='disabled')
        self.widget.see('end')  # Auto-scroll

    def flush(self):
        pass
if __name__ == "__main__":
    app = App()
    app.mainloop()
