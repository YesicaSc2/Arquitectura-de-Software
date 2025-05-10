# -------------------- PATRÓN CREACIONAL: SERVICE LOCATOR --------------------

class ServiceLocator:
    servicios = {}

    @staticmethod
    def registrar(nombre, servicio):
        ServiceLocator.servicios[nombre] = servicio

    @staticmethod
    def obtener(nombre):
        return ServiceLocator.servicios.get(nombre)

class ServicioPago:
    def procesar_pago(self, monto):
        print(f"Pago realizado por {monto} Bs.")

class ServicioDescuento:
    def aplicar_descuento(self, precio):
        return precio * 0.9  

ServiceLocator.registrar("pago", ServicioPago())
ServiceLocator.registrar("descuento", ServicioDescuento())

# -------------------- PATRÓN ESTRUCTURAL: ADAPTER --------------------

class CorreoExterno:
    def enviar_correo(self, mensaje):
        print(f"Correo externo enviado: {mensaje}")

class NotificadorAdapter:
    def __init__(self, correo):
        self.correo = correo

    def enviar(self, mensaje):
        self.correo.enviar_correo(mensaje)

# -------------------- PATRÓN DE COMPORTAMIENTO: OBSERVER --------------------

class FuncionTeatro:
    def __init__(self, obra):
        self.obra = obra
        self.observadores = []

    def agregar_usuario(self, usuario):
        self.observadores.append(usuario)

    def notificar_usuarios(self):
        for usuario in self.observadores:
            usuario.actualizar(self.obra)

    def nueva_funcion(self):
        print(f"\nNueva función agregada: {self.obra}")
        self.notificar_usuarios()

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, obra):
        print(f"{self.nombre}, hay una nueva función de: {obra}")


if __name__ == "__main__":

    servicio_pago = ServiceLocator.obtener("pago")
    servicio_descuento = ServiceLocator.obtener("descuento")

    precio_base = 100
    precio_final = servicio_descuento.aplicar_descuento(precio_base)
    print(f"\nPrecio con descuento: {precio_final} Bs")
    servicio_pago.procesar_pago(precio_final)


    correo_externo = CorreoExterno()
    notificador = NotificadorAdapter(correo_externo)
    notificador.enviar("Gracias por comprar tu entrada.")


    funcion = FuncionTeatro("Hamlet")
    usuario1 = Usuario("Luis")
    usuario2 = Usuario("Ana")

    funcion.agregar_usuario(usuario1)
    funcion.agregar_usuario(usuario2)

    funcion.nueva_funcion()
