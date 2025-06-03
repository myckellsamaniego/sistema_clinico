# models/interfaz_persona.py

from abc import ABC, abstractmethod

class Persona(ABC):
    """
    Clase abstracta que representa a una persona en el sistema.
    No puede instanciarse directamente.
    """

    def __init__(self, nombre: str, apellido: str, dni: str, telefono: str):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._telefono = telefono

    @abstractmethod
    def mostrar_info(self) -> str:
        """
        Método abstracto que deben implementar las subclases
        para mostrar su información específica.
        """
        pass
