try:
    # para python 3
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
except ImportError:
    # para python 2
    import Tkinter as tk
    from tkFileDialog import askopenfilename


import analizador_lexico as mod_al
import logging
import io

# Crear el logger
logger = logging.getLogger('main_logger')
logger.setLevel(logging.INFO)


# Crear un manipulador de archivos
fh = logging.FileHandler('aplicacion.log', mode='w')
fh.setLevel(logging.INFO)


# Adicionar el manipulador al logger
logger.addHandler(fh)




class GUI():
    resultado: str = ''
    ruta_archivo: str = ''
    codigo: str = ''


    def __init__(self, analizador: mod_al.AnalizadorLexico, parent=tk.Tk()):

        self.analizador = analizador

        self.ventana = parent
        self.ventana.title("Analizador de Codigo Dart")

        # configuraciones para la fila y columna
        self.ventana.rowconfigure(0, minsize=800, weight=1)
        self.ventana.columnconfigure(1, minsize=400, weight=1)
        self.ventana.columnconfigure(2, minsize=400, weight=1)

        # se crean los widgets necesarios para mostrar en la aplicacion
        self.txt_codigo = tk.Text(self.ventana,state='disabled')
        self.txt_resultados = tk.Text(self.ventana, state='disabled', wrap=tk.WORD)
        self.frm_botones = tk.Frame(self.ventana)
        self.btn_abrir = tk.Button(
            self.frm_botones,
            text='Abrir',
            command=self.abrir_archivo)

        #asignar los dos botones al marco frm_botones
        self.btn_abrir.grid(row=0, column=0, sticky='ew', padx=5, pady=5)


        self.frm_botones.grid(row=0, column=0, sticky='ns')
        self.txt_codigo.grid(row=0, column=1, sticky='nsew')
        self.txt_resultados.grid(row=0, column=2, sticky='nsew')

        self.ventana.mainloop()

    def abrir_archivo(self):

        # utilizar askopenfilename del modulo de filedialog para mostrar
        # un dialogo de abrir archivo y guardarlo en ruta_archivo
        self.ruta_archivo = askopenfilename(
            filetypes=[('Text Files', '*.txt')]
        )
        # verificar si el usuario cerro el cuadro de dialogo o
        # cliqueo en el boton cancelar en caso afirmativo se retoma sin ejecutar
        if not self.ruta_archivo:
            return
        else:
            fh.close()
            logger.info("Analizando un nuevo archivo")


        # se borra el contenido actual del cuadro de dialogo y el atributo codigo
        self.codigo = None
        self.analizador.limpiar()
        self.txt_codigo.configure(state='normal')
        self.txt_codigo.delete('1.0', tk.END)
        self.txt_resultados.delete('1.0', tk.END)
        # se abre el archivo en modo lectura y se guarda el codigo como string
        with open(self.ruta_archivo, "r") as archivo_entrado:
            self.codigo = archivo_entrado.read()
            # se inserta el codigo al widget de texto
            self.txt_codigo.insert(tk.END, self.codigo)
            self.txt_codigo.configure(state='disabled')
            for linea in self.codigo.splitlines():
                self.analizador.analizar_linea(linea)
            self.analizador.verificar_balances()


        with open('aplicacion.log','r') as archivo_log:
            self.resultado = archivo_log.read()
            self.txt_resultados.configure(state='normal')
            self.txt_resultados.delete('1.0', tk.END)
            self.txt_resultados.insert(tk.END, self.resultado)
            self.txt_resultados.configure(state='disabled')

        self.ventana.title(f"Analizador de Codigo Dart - {self.ruta_archivo}")


    def muestra_resultado(self, texto):
        self.txt_resultados.configure(state='normal')
        self.txt_resultados.delete('1.0', tk.END)
        self.txt_resultados.insert(tk.END, texto)
        self.txt_resultados.insert(tk.END,self.analizador.retornar_lista())
#        self.txt_resultados.insert(tk.END, self.analizador.retornar_texto())
        self.txt_resultados.configure(state='disabled')








if __name__=='__main__':
    analizador_lex = mod_al.AnalizadorLexico()
    gui = GUI(analizador_lex)

