
# Stiven De La Rosa Brito #20220457

import tkinter as tk  # Importa la librería tkinter para crear la interfaz gráfica
from tkinter import messagebox  # Importa el módulo messagebox de tkinter para mostrar mensajes
from queue import Queue  # Importa la clase Queue de la librería estándar para crear una cola FIFO

class SimuladorBanco:
    def __init__(self, root):
        """
        Inicializa el simulador del banco.
        
        Args:
            root: La ventana principal de la aplicación.
        """
        self.root = root  # Guarda la ventana principal
        self.cola_clientes = Queue()  # Inicializa una cola para almacenar los clientes
        self.create_widgets()  # Crea y muestra los widgets en la interfaz gráfica

    def create_widgets(self):
        """
        Crea y muestra los widgets en la interfaz gráfica.
        """
        # Título del programa
        self.label_title = tk.Label(self.root, text="Simulador de Banco", font=("Arial", 24, "bold"), pady=10)
        self.label_title.pack()

        # Frame para los campos de entrada y botones
        self.frame_input = tk.Frame(self.root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.frame_input.pack(fill=tk.X)

        # Etiqueta y entrada para el nombre del cliente
        self.label_input = tk.Label(self.frame_input, text="Nombre del Cliente:", font=("Arial", 14))
        self.label_input.grid(row=0, column=0, padx=5)

        self.entry = tk.Entry(self.frame_input, width=30, font=("Arial", 14))
        self.entry.grid(row=0, column=1, padx=5)

        # Botones para agregar cliente y atender cliente
        self.btn_llegada = tk.Button(self.frame_input, text="Agregar Cliente", command=self.agregar_cliente, bg="lightblue", font=("Arial", 14))
        self.btn_llegada.grid(row=0, column=2, padx=10)

        self.btn_atencion = tk.Button(self.frame_input, text="Atender Cliente", command=self.atender_cliente, bg="lightcoral", font=("Arial", 14))
        self.btn_atencion.grid(row=0, column=3, padx=10)

        # Frame para mostrar la lista de clientes en espera
        self.frame_cola = tk.Frame(self.root, bd=2, relief=tk.GROOVE, padx=10, pady=10)
        self.frame_cola.pack(fill=tk.BOTH, expand=True)

        self.label_cola = tk.Label(self.frame_cola, text="Clientes en Espera:", font=("Arial", 16, "bold"))
        self.label_cola.pack()

        self.text_cola = tk.Text(self.frame_cola, height=10, width=50, font=("Arial", 12))
        self.text_cola.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_cola = tk.Scrollbar(self.frame_cola, orient=tk.VERTICAL, command=self.text_cola.yview)
        self.scrollbar_cola.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_cola.config(yscrollcommand=self.scrollbar_cola.set)

        # Impide que la ventana se pueda maximizar
        self.root.resizable(False, False)

        # Centrar la ventana en la pantalla
        self.center_window()

    def center_window(self):
        """
        Centra la ventana en la pantalla.
        """
        # Obtiene el tamaño de la ventana y de la pantalla
        window_width = 900
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Establece la posición de la ventana en el centro de la pantalla
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def agregar_cliente(self):
        """
        Agrega un cliente a la cola de espera.
        """
        nombre_cliente = self.entry.get()
        if nombre_cliente:
            self.cola_clientes.put(nombre_cliente)
            self.mostrar_lista_clientes()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa el nombre del cliente.")

    def atender_cliente(self):
        """
        Atiende al cliente que está al principio de la cola.
        """
        if not self.cola_clientes.empty():
            cliente_atendido = self.cola_clientes.get()
            messagebox.showinfo("Cliente Atendido", f"Se atendió a: {cliente_atendido}")
            self.mostrar_lista_clientes()
        else:
            messagebox.showwarning("Advertencia", "No hay clientes esperando.")

    def mostrar_lista_clientes(self):
        """
        Muestra la lista de clientes en espera en el área de texto.
        """
        self.text_cola.delete(1.0, tk.END)
        for i, cliente in enumerate(list(self.cola_clientes.queue), start=1):
            self.text_cola.insert(tk.END, f"{i}. {cliente}\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Simulador de Banco")
    root.configure(bg="white")
    app = SimuladorBanco(root)
    root.mainloop()
