class TV:

    _numTV=0

    def __init__(self, marca, estado):
        from televisores.control import Control
        from televisores.marca import Marca
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV.setNumTV(TV.getNumTV() +1)

    def setMarca(self, marca):
        self._marca = marca
    def getMarca(self):
        return self._marca

    def setControl(self, control):
        self._control = control
    def getControl(self):
        return self._control

    def setPrecio(self, precio):
        self._precio = precio
    def getPrecio(self):
        return self._precio

    def setCanal(self, canal):
        if (self._estado) and (1<= canal and canal <= 120):
            self._canal = canal
        else:
            pass

    def getCanal(self):
        return self._canal

    def setVolumen(self, volumen):
        if (self._estado) and (volumen >=0 and volumen <=7):
            self._volumen = volumen
        else:
            pass

    def getVolumen(self):
        return self._volumen

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    @classmethod
    def setNumTV(cls, nuevoNumTV):
        cls._numTV = nuevoNumTV

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        self.setCanal(self.getCanal() +1)

    def canalDown(self):
        self.setCanal(self.getCanal() -1)

    def volumenUp(self):
        self.setVolumen(self.getVolumen() +1)

    def volumenDown(self):
        self.setVolumen(self.getVolumen() -1)

    def getEstado(self):
        return self._estado
