from abc import ABC, abstractmethod
from logger.logger_config import logger

class BaseDatos(ABC):
    def __init__(self):
        """
        Constructor de la clase base BaseDatos. Inicializa la conexión y el cursor de la base de datos como None.
        """
        self._conn = None
        self._cursor = None
        logger.debug("BaseDatos initialized")

    @abstractmethod
    def conectar(self):
        """
        Método abstracto para conectar a la base de datos.
        Debe ser implementado por las clases derivadas.
        """
        pass

    @abstractmethod
    def crear(self, *args, **kwargs):
        """
        Para crear un nuevo registro en la base de datos.
        Debe ser implementado por las clases derivadas.
        """
        pass

    @abstractmethod
    def leer(self, *args, **kwargs):
        """
        Para leer registros de la base de datos.
        Debe ser implementado por las clases derivadas.
        """
        pass

    @abstractmethod
    def actualizar(self, *args, **kwargs):
        """
        Para actualizar un registro existente en la base de datos.
        Debe ser implementado por las clases derivadas.
        """
        pass

    @abstractmethod
    def borrar(self, *args, **kwargs):
        """
        Para borrar un registro de la base de datos.
        Debe ser implementado por las clases derivadas.
        """
        pass

    def cerrar(self):
        """
        Cierra el cursor y la conexión de la base de datos si están abiertos.
        """
        if self._cursor:
            self._cursor.close()
        if self._conn:
            self._conn.close()
        logger.debug("BaseDatos connection closed")
