import colorama

class Constantes:

    """Clase donde se almacenan todas las constantes del programa"""

    MSG = 'msg.txt'

    #Sistemas operativos y comandos
    WINDOWS = 'windows'
    LINUX = 'linux'
    CLS = 'csl'
    CLEAR = 'clear'

    #Claves de acceso
    PIN_MESSAGE = 'Ingresa tu PIN :)\t'
    PIN = '1235'
    PIN_NOT_MATCH = 'PIN Incorrecto'
    CLOSE_PROGRAM = 'Se realizaron 3 intentos incorrectos, limite maximo.\nCerrando el programa :('
    
    #Info general
    NAME = 'Nombre: '
    SALDO = 'Saldo: '
    DATE = 'Fecha: '
    HOUR = 'Hora: '
    S_ANTERIOR = 'Saldo Anterio. '
    S_ACTUAL = 'Saldo Actural: '
    RETIRO = 'Saldo retirado: '


    #numeros
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    ONE_THOUSAND = 1000.00

    #Signos
    ASTERISK = '*'
    QUESTION = '?'
    PESOS = '$'
    UNDERSCORE = '-'*20

    #Formatos
    F_DATE = '%y-%m-%d'
    F_HOUR = '%H:%M:%S'

    #Mensaje de bienvenida
    WELCOME = 'BIENVENIDO '
    OPTIONS = '1. Consulta Saldo\n2. Retirar Saldo\n3. Histórico de movimientos\n4. Salir'
    USER_REQUEST = 'Que deseas hacer '
    SALDO_MESSAGE = 'Tu saldo es de:'
    VALUE_CASH = 'Ingresa el monto a retirar, por favor.\t'
    MESSAGE_MONEY = 'No elvide tomar su dinero :)'
    QUERY = f'{ASTERISK*10}CONSULTA DE SALDO{ASTERISK*10}'
    RETIRAR = f'{ASTERISK*10}RETIRAR SALDO{ASTERISK*10}'
    QUIT = 'Presiona cualquier tecla para regresar al menu principal o (salir) para terminar\t'
    EXIT = 'salir'

    #errores
    OPTION_NOT_FOUND = 'Lo siento, la opcion no es valida, intentalo de nuevo!'
    VALUE_ERROR = 'Lo siento, el monto no es valido, intentalo de nuevo!'
    NO_MONEY = 'Lo siento, su saldo es inferior a lo solicitado'

    #Historico
    HISTORY = f'{ASTERISK*10}HISTORIAL DE MOVIMIENTOS{ASTERISK*10}'

    SUCCESS = 'Operación Existosa!'

