# Reconocedor de Dígitos con la Data MNIST

![MNIST Digits](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)

Este proyecto utiliza un modelo de red neuronal convolucional (CNN) para reconocer dígitos escritos a mano del famoso conjunto de datos [MNIST](http://yann.lecun.com/exdb/mnist/). El modelo es capaz de identificar correctamente los números del 0 al 9 con una alta precisión.

## Descripción

El conjunto de datos MNIST contiene 70,000 imágenes de dígitos escritos a mano (60,000 para entrenamiento y 10,000 para prueba), donde cada imagen tiene un tamaño de 28x28 píxeles en escala de grises. El objetivo de este proyecto es entrenar un modelo que pueda clasificar estas imágenes con precisión.

### Características principales:
- **Modelo:** Red Neuronal Convolucional (CNN)
- **Precisión esperada:** > 98%
- **Librerías usadas:** `TensorFlow`, `Keras`, `NumPy`, `Matplotlib`

## Requisitos

- Python 3.x
- TensorFlow 2.x
- Keras
- NumPy
- Matplotlib

Instalar los paquetes necesarios:
```bash
pip install tensorflow keras numpy matplotlib
