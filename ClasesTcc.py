class Cliente:

    def __init__(self, idCliente, nombre, numero):
        self.id_cliente = idCliente
        self.nombre = nombre
        self.numero = numero

    def __str__(self):
        return f"Cliente[ID: {self.id_cliente}, Nombre: {self.nombre}, Contacto: {self.numero}]"

class Tecnico:

    def __init__(self, idTecnico, nombre, especialidad):
        self.idTecnico = idTecnico
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Técnico[ID: {self.idTecnico}, Nombre: {self.nombre}, Especialidad: {self.especialidad}]"

class Servicio:

    def __init__(self, idServicio, descripcion, costo):
        self.idServicio = idServicio
        self.descripcion = descripcion
        self.costo = costo

    def __str__(self):
        return f"Servicio[ID: {self.idServicio}, Descripción: {self.descripcion}, Costo: {self.costo}]"

class OrdenDeTrabajo:

    def __init__(self, idOrden, cliente, tecnico, servicio):
        self.idOrden = idOrden
        self.cliente = cliente
        self.tecnico = tecnico
        self.servicio = servicio
        self.estado = "Pendiente"

    def actualizarEstado(self, nuevoEstado):
        self.estado = nuevoEstado

    def __str__(self):
        return (f"OrdenDeTrabajo[ID: {self.idOrden}, Cliente: {self.cliente.nombre}, "
                f"Técnico: {self.tecnico.nombre}, Servicio: {self.servicio.descripcion}, Estado: {self.estado}]")

# objetos de cada clase;
cliente1 = Cliente(1, "Felix Velazques", "3012892860")
tecnico1 = Tecnico(1, "Gabriel Valeta", "Reparación de electrodomésticos")
servicio1 = Servicio(1, "Reparación de lavadora", 150.00)

# objeto de la clase orden de trabajo
orden1 = OrdenDeTrabajo(1, cliente1, tecnico1, servicio1)

# hacer print a los objetos;
print(cliente1)
print(tecnico1)
print(servicio1)
print(orden1)

# actualizar el estado estado(opcional)
orden1.actualizarEstado("Completada")
print(orden1)
