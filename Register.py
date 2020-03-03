class Register(object):

    reg_size = 32
    data_size = 8
    registers = [0] * reg_size
    data = [0] * data_size
    used_data = [0] * data_size
    used_data2 = 0
    stur_exists = False
    byte = 4
    branch = 0
    null_data = True
    bbreak = False
    c = 0
    pc = 4

    def resize(self, register2, address):

        while ((self.registers[register2] + (address * self.byte)) / self.byte > self.data_size):
               self.data_size += 8

        temp = [None] * self.data_size
        temp2 = [None] * self.data_size

        for i in range(0 , len(self.data)):
            temp[i] = self.data[i]
            temp2[i] = self.used_data[i]

        self.data = temp
        self.used_data = temp2

    def resizeData(self):

        self.data_size += 8

        temp = [0] * (self.data_size)
        temp2 = [0] * (self.data_size)

        for i in range(0 , len(self.data)):
            
            temp[i] = self.data[i]
            temp2[i] = self.used_data[i]

        self.data = temp
        self.used_data = temp2

    def addRegister(self, register1, register2 , register3):
        self.registers[register1] = self.registers[register2] + self.registers[register3]

    def andRegister(self, register1, register2 , register3):
        self.registers[register1] = self.registers[register2] & self.registers[register3]

    def orrRegister(self, register1, register2 , register3):
        self.registers[register1] = (self.registers[register2] | self.registers[register3])

    def subRegister(self, register1, register2 , register3):
        self.registers[register1] = self.registers[register2] - self.registers[register3]

    def lslRegister(self,register1, register2, shamt):
        self.registers[register1] = (self.registers[register2] << shamt)

    def asrRegister(self,register1, register2, shamt):
        self.registers[register1] = (self.registers[register2] >> shamt)

    def lsrRegister(self, register1, register2, shamt):
        self.registers[register1]= (self.registers[register2] % (1 << 64)) >> shamt

    def eorRegister(self, register1, register2 , register3):
        self.registers[register1] = (self.registers[register2] ^ self.registers[register3])

    def nopRegister(self, register1, register2 , register3):
        None

    def addImmediate(self, register1, register2 ,  value ):
        self.registers[register1] = self.registers[register2] + value

    def subImmediate(self, register1, register2 , value):
        self.registers[register1] = self.registers[register2] - value

    def sturAddress(self , register1, register2, address):

         if (self.bbreak == True):
            
            if (self.dataIsMax(register2 , address) == True):
                 self.resize(register2, address)

            self.data[(self.registers[register2] + address * self.byte) / self.byte] = self.registers[register1]
            self.used_data[(self.registers[register2] + address* self.byte) / self.byte] = True
            self.null_data = False

         else:
             None

    def ldurAddress(self , register1, register2 , address):
        
        if (self.bbreak == True):
            if (self.dataIsMax(register2 , address) == True or self.addressIsEmpty(register2 , address) == True):
                print "LDUR Error: address at requested register is Empty!!!"

            else:
                self.registers[register1] = self.data[(self.registers[register2] + address * self.byte) / self.byte]

    def cbzAddress(self , register1 , cbrAddress ):

        if (self.registers[register1] == 0):
            return cbrAddress
        
        else:
            return 0

    def cbnzAddress(self , register1 , cbrAddress ):

        if (self.registers[register1] != 0):
            return cbrAddress
        
        else:
            return 0

    def addMOVK(self, register1 , value , shamt):
        self.registers[register1] = self.registers[register1] + (value << shamt)

    def addMOVZ(self, register1 , value , shamt):
        self.registers[register1] = (value << shamt)

    def addData(self, value, byte):

        if (self.used_data2 >= self.data_size):
            self.resizeData()

        self.data[self.used_data2] = value
        self.used_data[self.used_data2] = True

        self.used_data2 += 1
        self.null_data = False

    def addressIsEmpty(self , register2 , address):
        return (self.used_data[(self.registers[register2] + address * self.pc) / self.pc] == None)

    def dataIsMax(self , register2 , address):
        return ((self.registers[register2] + address * self.byte) / self.pc > self.data_size)

    def resetRegistrs(self):
        
        for i in range(0 , len(self.registers)):
             self.registers[i] = 0

    def returnRegisters(self , min , max):

        s = ""
        
        for i in range(min , max):
              s += str(self.registers[i]).center(8)

        return s

    def printData(self):

        s =""

        if (self.dataIsNone() == False):

            for i in range(0, self.data_size):
                if not self.data[i]:
                    self.data[i] = 0

            for i in xrange(0, self.data_size, 8):
                s += str(i * 4).center(3) + ":" + "".join(str(j).center(6) for j in self.data[i:i+8]) + "\n"

            return s

        else:
            return ""

    def dataIsNone(self):
        return (self.null_data == True)

    def breakIsTrue(self):
        self.bbreak = True




