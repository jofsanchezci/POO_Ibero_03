
# Conceptos Básicos de POO: Abstracción y Encapsulamiento

## 1. Abstracción

La **abstracción** es el proceso de ocultar los detalles de implementación de un objeto y exponer solo las características esenciales que el usuario necesita conocer. Esto permite que los programadores se centren en la interacción con los objetos, sin preocuparse por cómo están implementados internamente.

- **Objetivo**: Simplificar la interacción con el objeto, mostrando solo lo relevante.

### Ejemplo en Python:
```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando.")
    
    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando.")
```
Aquí, el comportamiento de arrancar y frenar está **abstraído**. El usuario solo necesita llamar a los métodos sin entender cómo exactamente el coche arranca o frena.

## 2. Encapsulamiento

El **encapsulamiento** se refiere a la ocultación de los detalles internos de un objeto, protegiendo sus datos y permitiendo que solo ciertos métodos accedan y modifiquen esos datos. Este enfoque asegura que los atributos internos de un objeto no sean alterados directamente desde fuera de la clase, sino que solo se puedan modificar a través de métodos que puedan validar los datos.

- **Objetivo**: Proteger los datos de un objeto y controlar el acceso a ellos.

### Ejemplo en Python:
```python
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depositados {monto} unidades.")
        else:
            print("Monto no válido.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retirados {monto} unidades.")
        else:
            print("Fondos insuficientes o monto no válido.")

    def obtener_saldo(self):
        return self.__saldo
```
En este ejemplo, el atributo `__saldo` está **encapsulado**, lo que significa que no puede ser modificado directamente desde fuera de la clase. El acceso a este atributo solo se hace a través de los métodos `depositar()`, `retirar()` y `obtener_saldo()`.

## Resumen de las diferencias:

- **Abstracción**: Oculta la complejidad, mostrando solo lo que es necesario y relevante para el usuario.
- **Encapsulamiento**: Protege los datos y permite que el acceso a ellos esté controlado y validado mediante métodos.

## Ejemplos.
- Consultar los ejemlos de tipos de datos en Python.
- Consultar el geter seter en java.
- Los programas estan en el repositorio.

