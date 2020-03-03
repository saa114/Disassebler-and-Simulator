import Register

class IFormat(object):

    OPCODE_LENGTH = 10
    INSTRUCTION_LENGTH = 32
    instruction_name = 0
    opcode = ""
    opcode_field = ""
    alu_field = ""
    rn_field = 0
    rd_field = 0
    rnMask = 0x3E0
    rdMask = 0x1F
    aluMask = 0x3FFC00
    instruction = 0
    immediate = ""
    isNegative = False
    instruction1 = [] * 32
    _reg = None

    def __init__(self , MyList , reg):

       for x in range(0 , self.INSTRUCTION_LENGTH - 1 ):
            self.instruction = ''.join(str(e) for e in MyList)

       self._reg = reg

    def getOpcode(self):

       self.opcode = self.instruction[0:11]
       self.opcode = int(self.opcode, 2)

       if (self.opcode == 1160 or self.opcode == 1161 ):

            self.opcode_field = "ADDI"
            self._reg.addImmediate(self.getRDfield(), self.getRNField(), self.getALUField())


       elif (self.opcode == 1672 or self.opcode == 1673):

            self.opcode_field = "SUBI"
            self._reg.subImmediate(self.getRDfield(), self.getRNField(), self.getALUField())

       else:
           pass

       return self.opcode_field

    def getALUField(self):

        self.alu_field = ""
        if (self.instruction[10] == "1"):

            for i in range(0 , len(self.instruction)) :

                    if (self.instruction[i] == "1"):

                        self.alu_field += "0"

                    else:
                        self.alu_field += "1"


            return  -(((int(self.alu_field, 2) & self.aluMask) >> 10)  + 1)

        else:

            return (int(self.instruction, 2) & self.aluMask) >> 10


    def getRNField(self):
        return (int(self.instruction, 2) & self.rnMask) >> 5


    def getRDfield(self):
        return (int(self.instruction, 2) & self.rdMask) >> 0


    def getTranslation(self):
       return (str(self.getOpcode()) + "   " + "R" + str(self.getRDfield()) +\
                               "," + " " + "R" + str(self.getRNField()) + "," + " " + \
                               "#" + str(self.getALUField()))




