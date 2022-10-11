import platform
import datetime as dt
from datetime import datetime
from Constantes import Constantes as cons

class User:

    """Clase que reprenta el usuario del cajero automatico"""

    def __init__(self):

        """Constructor de la clase"""

        self.__saldo = cons.ONE_THOUSAND
        self.__historico = []

    def name(self):
        """Se obtiene el nombre del usuario de la maquina que representara
        el nombre del usuario en el cajero automatico

        Args:
            params: None
        Returns:
            (string) Nombre del host"""

        return platform.node()

    @property
    def saldo(self):

        """Consulta el saldo acutal del usuario

        Args:
            params: None

        Return:
            (float) Monto total"""

        return  float(self.__saldo)

    @saldo.setter
    def saldo(self,saldo):

        """Establce el saldo actual de acuerdo a los movimientos del usuario

        Args:
            param1: (decimal) Monto a modificar"""

        self.__saldo = saldo

    @property
    def historico(self):

        """Obtiene la lista de historicos de los movimientos hechos por el usuario

        Args:
            None
        Return:
            Lista de historico"""

        return self.__historico

    @historico.setter
    def historico(self,historico):

        """Registra los movimientos hechos por el usuario asi como,
        hora, minutos y segundos

        Args:
            param1: (decimal) saldo retirado

        Return
            None"""

        now = dt.datetime.now()
        s_anterior = historico+self.saldo

        lst = [
            datetime.strftime(now,cons.F_DATE),
            datetime.strftime(now,cons.F_HOUR),
            s_anterior,
            historico,
            self.saldo]
        self.__historico.append(lst)
