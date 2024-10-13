import numpy as np
import cv2
import tkinter as tk
from tensorflow.keras.models import load_model
from PIL import Image, ImageTk

# Cargar el modelo
model = load_model('modelo_digit_recognizer.h5')

# Función para predecir el dígito
def predict_digit():
    # Obtener la imagen del lienzo
    img = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises

    # Invertir los colores
    img = 255 - img  # Invertir colores (dígito blanco a negro, fondo negro a blanco)

    # Procesar la imagen
    img = cv2.resize(img, (28, 28))  # Redimensionar a 28x28
    img = img / 255.0  # Normalizar
    img = img.reshape(1, 28, 28, 1)  # Ajustar dimensiones para el modelo

    # Hacer la predicción
    prediction = model.predict(img)
    digit = np.argmax(prediction)  # Obtener el dígito predicho

    # Mostrar el resultado
    result_label.config(text=f'Predicción: {digit}')

    # Mostrar la imagen que se predice
    cv2.imshow('Imagen para predecir', img[0, :, :, 0])  # Mostrar la imagen
    cv2.waitKey(0)  # Esperar a que se presione una tecla
    cv2.destroyAllWindows()  # Cerrar la ventana

# Función para limpiar el lienzo
def clear_canvas():
    global canvas
    canvas = np.ones((200, 200, 3), dtype=np.uint8) * 255  # Lienzo blanco
    update_canvas()  # Actualizar el lienzo

# Función para actualizar el lienzo en la interfaz
def update_canvas():
    image = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)  # Convertir a RGB
    img = Image.fromarray(image)  # Crear una imagen de PIL
    img = img.resize((200, 200), Image.LANCZOS)  # Ajustar el tamaño

    # Convertir a formato que Tkinter pueda mostrar
    img_tk = ImageTk.PhotoImage(img)

    canvas_widget.create_image(0, 0, image=img_tk, anchor=tk.NW)  # Mostrar lienzo
    canvas_widget.image = img_tk  # Mantener referencia de la imagen

# Funciones para manejar el dibujo con el mouse
def paint(event):
    x, y = event.x, event.y
    cv2.circle(canvas, (x, y), 10, (0, 0, 0), -1)  # Dibujar un círculo negro

    # Actualizar el lienzo
    update_canvas()

# Crear la ventana principal
window = tk.Tk()
window.title("Reconocedor de Dígitos")

# Crear el lienzo
canvas = np.ones((200, 200, 3), dtype=np.uint8) * 255  # Lienzo blanco
canvas_widget = tk.Canvas(window, width=200, height=200, bg='white')
canvas_widget.pack()

# Crear un botón para hacer la predicción
predict_button = tk.Button(window, text='Predecir Dígito', command=predict_digit)
predict_button.pack()

# Crear un botón para limpiar el lienzo
clear_button = tk.Button(window, text='Limpiar', command=clear_canvas)
clear_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(window, text='Predicción:')
result_label.pack()

# Inicializar el lienzo
clear_canvas()

# Configurar eventos del mouse para dibujar
canvas_widget.bind("<B1-Motion>", paint)  # Dibujar mientras se mantiene presionado el botón izquierdo del mouse

# Ejecutar la aplicación
window.mainloop()
