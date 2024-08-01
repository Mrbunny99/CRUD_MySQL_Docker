import mysql.connector
from baseDatos.base_datos import BaseDatos
from logger.logger_config import logger

class PlanetaDB(BaseDatos):
    def __init__(self, host, user, password, database):
        """
        Constructor de la clase PlanetaDB.

        host: Dirección del servidor MySQL
        user: Nombre de usuario de MySQL
        password: Contraseña del usuario de MySQL
        database: Nombre de la base de datos a conectar
        """
        super().__init__()
        self._host = host
        self._user = user
        self._password = password
        self._database = database
        self.conectar()

    def conectar(self):
        """
        Conecta a la base de datos y crea un cursor.
        """
        try:
            self._conn = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            self._cursor = self._conn.cursor()
            logger.info("Conexión exitosa a la base de datos")
        except mysql.connector.Error as err:
            logger.error(f"Error: {err}")

    def crear(self, nombre, tipo, radio, distancia_sol):
        """
        Crea un nuevo registro en la tabla.

        nombre: Nombre del planeta
        tipo: Tipo del planeta (Rocoso, Gaseoso, etc.)
        radio: Radio del planeta
        distancia_sol: Distancia del planeta al sol
        """
        try:
            sql = "INSERT INTO planeta (nombre, tipo, radio, distancia_sol) VALUES (%s, %s, %s, %s)"
            val = (nombre, tipo, radio, distancia_sol)
            self._cursor.execute(sql, val)
            self._conn.commit()
            logger.info(f"Planeta {nombre} creado correctamente")
        except mysql.connector.Error as err:
            logger.error(f"Error: {err}")

    def leer(self, id=None):
        """
        Lee registros de la tabla. Si se ingresa un ID, ubica el id ingresado.

        id: ID del planeta a leer
        """
        try:
            if id:
                sql = "SELECT * FROM planeta WHERE id = %s"
                self._cursor.execute(sql, (id,))
            else:
                sql = "SELECT * FROM planeta"
                self._cursor.execute(sql)
            resultados = self._cursor.fetchall()
            logger.info(f"Leídos {len(resultados)} planetas")
            return resultados
        except mysql.connector.Error as err:
            logger.error(f"Error: {err}")
            return []

    def actualizar(self, id, nombre, tipo, radio, distancia_sol):
        """
        Actualiza un registro en la tabla

        id: ID del planeta a actualizar
        nombre: Nuevo nombre del planeta
        tipo: Nuevo tipo del planeta
        radio: Nuevo radio del planeta
        distancia_sol: Nueva distancia del planeta al sol
        """
        try:
            sql = "UPDATE planeta SET nombre = %s, tipo = %s, radio = %s, distancia_sol = %s WHERE id = %s"
            val = (nombre, tipo, radio, distancia_sol, id)
            self._cursor.execute(sql, val)
            self._conn.commit()
            logger.info(f"Planeta con id {id} actualizado correctamente")
        except mysql.connector.Error as err:
            logger.error(f"Error: {err}")

    def borrar(self, id):
        """
        Borra un registro de la tabla.

        id: ID del planeta a borrar
        """
        try:
            sql = "DELETE FROM planeta WHERE id = %s"
            self._cursor.execute(sql, (id,))
            self._conn.commit()
            logger.info(f"Planeta con id {id} borrado correctamente")
        except mysql.connector.Error as err:
            logger.error(f"Error: {err}")
