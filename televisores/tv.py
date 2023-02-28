class TV:
    _numTv=0
    def__init__(self, marca, estado):
        from televisores.control import control
        from televisores.marca import Marca
        self._marca = marca
        sel._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        tv.setNumTV(TV.getNumTV()+1)

    def setMarca(self, marca):
        self._marca = marca
    def getMarca(self):
        return self._marca

    def setControl(self, control):
        self._control = control
    def getControl(self):
        return self._control

    def setPrecio(self, precio):
        self._precio = _precio
    def getPrecio(self):
        return self._precio

    def setCanal(self, canal):
        if (self.estado) and (canal >=1 and canal <= 120)
            self._canal = canal
        else:
            pass

    def getCanal(self):
        return self._canal

    def setVolumen(self, volumen):
        if (self.estado) and (volumen >=0 and volumen <=7):
            self._volumen = volumen
        else:
            pass

    def getVolumen(self):
        return self._volumen

    @classmethod
    def getNumTV(cls):
        return cls.numTV

    @classmethod
    def setNumTV(cls, nuevoNumTV):
        cls.numTV = nuevoNumTV

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
        return self.estado
