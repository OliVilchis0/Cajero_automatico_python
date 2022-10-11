from User import User
from Constantes import Constantes as cons
import platform
import os
import time

class Cajero:

    """Clase que representa las funciones de un cajero automatico"""

    def __init__(self):
        pass

    def __call__(self):

        """Se inicializan los metodos pricipales"""

        self.msg()
        self.login()

    def login(self):

        """Pide el PIN del usuario para entrar a los movimientos"""

        for i in range(cons.ZERO,cons.THREE):

            pin = input(cons.PIN_MESSAGE)
            if pin == cons.PIN:
                self.options()
                break
            else:
                print(cons.CLOSE_PROGRAM) if i == cons.TWO else print(cons.PIN_NOT_MATCH)

    def options(self):

        """Imprime en pantalla el mensaje de bienvenida y las opciones que puede usar el usuario,
        para ello, se inicaializa la clase User, con el fin de obtener la informacion de este

        Args:
            parmas: None
        return:
            (print) Mensaje de opciones"""

        user = User()

        while True:
            self.msg()

            print(f'{cons.WELCOME}{user.name()}')
            print(cons.OPTIONS)

            try:
                option = int(input(f'{cons.USER_REQUEST}{user.name()}{cons.QUESTION}\t'))
            except:
                print(cons.OPTION_NOT_FOUND)
                time.sleep(cons.ONE)
                continue

            if option == cons.ONE:
                self.consultar_saldo(user.name(),user.saldo)
            elif option == cons.TWO:
                self.retirar_saldo(user)
            elif option == cons.THREE:
                self.historico(user)
            elif option == cons.FOUR:
                exit()
            else:
                print(cons.OPTION_NOT_FOUND)
                time.sleep(cons.TWO)

    def consultar_saldo(self,name,saldo):

        """Muestra en pantalla el saldo totol del usuario

        Args:
            param1: (string) Nombre del usuario
            param2: (float) Saldo total del usuario
        Returns:
            None"""

        self.msg()
        print(cons.QUERY)
        print(f'{cons.NAME} {name}')
        print(f'{cons.SALDO} {cons.PESOS}%.2f'%(saldo))
        option = input(cons.QUIT)

        if option.lower() == cons.EXIT:
            exit()

    def retirar_saldo(self,user):

        """Obtiene el monto a retirar y valida que este no sea mayo al existente
        en la cuenta

        Args:
            param1: (object) objeto usuario 
            param2: (input) monto a retirar
        Return:
            None"""

        self.msg()
        print(cons.RETIRAR)

        try:
            monto = float(input(cons.VALUE_CASH))
            saldo_actual = user.saldo
            if monto <= saldo_actual:
                user.saldo = saldo_actual - monto
                user.historico = monto
                print(cons.SUCCESS)
                print(cons.MESSAGE_MONEY)
            else:
                print(cons.NO_MONEY)
        except Exception as e:
            print(e)
            print(cons.VALUE_ERROR)
            time.sleep(cons.TWO)
            self.retirar_saldo(user)

        option = input(cons.QUIT)

        if option.lower() == cons.EXIT:
            exit()

    def historico(self,user):

        """Imprime el historial de retiros hechos por el usuario

        Args:
            param1: (Object) objeto usuario

        Returns:
            None"""

        self.msg()
        print(cons.HISTORY)

        for i in user.historico:
            print(f'{cons.DATE}{i[cons.ZERO]}')
            print(f'{cons.HOUR}{i[cons.ONE]}')
            print(f'{cons.S_ANTERIOR}{i[cons.TWO]}')
            print(f'{cons.RETIRO}{i[cons.THREE]}')
            print(f'{cons.S_ACTUAL}{i[cons.FOUR]}')
            print(cons.UNDERSCORE)

        option = input(cons.QUIT)

        if option.lower() == cons.EXIT:
            exit()

        option = input(cons.QUIT)

        if option.lower() == cons.EXIT:
            exit()

    def msg(self):

        """Mensaje Inicial del programa donde borra la pantalla y presenta el mensaje almacenado
        en el archivo msg.txt

        Args:
            params: None
        Return:
            String: Mensaje de bienvenida"""

        so = platform.system()
        os.system(cons.CLS) if os == cons.WINDOWS else os.system(cons.CLEAR)

        with open(cons.MSG) as file:
            print(file.read())
