import mysql.connector

from contextlib import contextmanager
from dataclasses import dataclass
import dbt.exceptions # noqa
from dbt.adapters.base import Credentials

from dbt.adapters.sql import SQLConnectionManager as connection_cls

from dbt.logger import GLOBAL_LOGGER as logger

logger = AdapterLogger("doris")


@dataclass
class DorisCredentials(Credentials):

    host: str = "127.0.0.1"
    port: int = 9030
    username: str = "root"
    password: str = ""
    database: Optional[str] = None
    schema: Optional[str] = None

    _ALIASES = {
        "dbname":"database",
        "pass":"password",
        "user":"username"
    }

    @property
    def type(self):
        return "doris"

    @property
    def unique_field(self):
        return self.host

    def _connection_keys(self):
        return ("host","port","username","schema")

class DorisConnectionManager(connection_cls):
    TYPE = "doris"


    @contextmanager
    def exception_handler(self, sql: str):
        try:
            yield
        except mysql.connector.DatabaseError as e:
            logger.debug(f"Doris error: {e}, sql: {sql}")
            raise exceptions.DatabaseException(str(e)) from e
        except Exception as e:
            logger.debug(f"Error running SQL: {sql}")
            if isinstance(e, exceptions.RuntimeException):
                raise e

    @classmethod
    def open(cls, connection):
        if connection.state == "open":
            logger.debug("Connection is already open, skipping open")
            return connection
        credentials = connection.credentials
        kwargs = {
            "host": credentials.host,
            "port": credentials.port,
            "user": credentials.username,
            "password": credentials.password,
        }
        try:
            connection.handle = mysql.connector.connect(**kwargs)
            connection.state = ConnectionState.OPEN
        except mysql.connector.Error as e:
            logger.debug(f"Error connecting to database: {e}")
            connection.handle = None
            connection.state = ConnectionState.FAIL
            raise exceptions.FailedToConnectException(str(e))
        return connection



    def begin(self):
        """
        https://doris.apache.org/docs/data-operate/import/import-scenes/load-atomicity/
        Doris's inserting always transaction, just ignore it
        """
        pass

    def commit(self):
        pass



    @classmethod
    def get_response(cls,cursor):
        code = "SUCCESS"
        num_rows = 0

        if cursor is not None and cursor.rowcount is not None:
            num_rows = cursor.rowcount

        # There's no real way to get the status from the mysql-connector-python driver.
        # So just return the default value.
        return AdapterResponse(
            _message="{} {}".format(code, num_rows), 
            rows_affected=num_rows, 
            code=code
        )



    def cancel(self, connection):
        connection.handle.close()

