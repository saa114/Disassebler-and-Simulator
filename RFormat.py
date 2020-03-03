import Register

class RFormat(object):

    OPCODE_LENGTH = 10
    INSTRUCTION_SIZE = 32
    instruction_name = ""
    opcode = ""
    opcode_field = ""
    rm_field = ""
    shamt_field = ""
    rn_field = ""
    rd_field = ""
    rmMask = 0x1F0000
    rnMask = 0x3E0
    rdMask = 0x1F
    shamtMask = 0xFC00
    instruction = ""
    _reg = None

    def __init__(self , MyList , reg ):

       for x in range(0 , self.INSTRUCTION_SIZE - 1):
            self.instruction = ''.join(str(e) for e in MyList)


       self._reg = reg


    def getOpcode(self,  *args ):

       self.opcode = self.instruction[0:11]
       self.opcode = int(self.opcode, 2)

       if (self.opcode == 1112 ):

            self.opcode_field = "ADD"
            self._reg.addRegister(self.getRDfield(), self.getRNField(),  self.getRMField())


       elif (self.opcode == 1104):

            self.opcode_field = "AND"
            self._reg.andRegister(self.getRDfield() , self.getRMField() ,  self.getRNField() )


       elif (self.opcode == 1360):

            self.opcode_field = "ORR"
            self._reg.orrRegister(self.getRDfield(), self.getRMField(), self.getRNField())


       elif (self.opcode == 1624):

            self.opcode_field = "SUB"
            self._reg.subRegister(self.getRDfield() , self.getRNField(),  self.getRMField())

       elif (self.opcode == 1690):

            self.opcode_field = "LSR"
            self._reg.lsrRegister(self.getRDfield(), self.getRNField(), self.getShamtfield())

       elif (self.opcode == 1691):

            self.opcode_field = "LSL"
            self._reg.lslRegister(self.getRDfield(), self.getRNField() , self.getShamtfield())

       elif (self.opcode == 1692):
            self.opcode_field = "ASR"
            self._reg.asrRegister(self.getRDfield(), self.getRNField(), self.getShamtfield())


       elif (self.opcode == 1872):

            self.opcode_field = "EOR"
            self._reg.eorRegister(self.getRDfield(), self.getRMField() , self.getRNField())

       elif (self.opcode == 0):
            self.opcode_field = "NOP"
       
       else:
           pass

       return self.opcode_field

    def getRMField(self):

        if (self.checkShamt() == False):
            return (int(self.instruction, 2) & self.rmMask) >> 16

        else:
            return ""

    def getShamtfield(self):

        self.shamt_field = (int(self.instruction , 2) & self.shamtMask) >> 10 
        return self.shamt_field

    def getRNField(self):
        return (int(self.instruction, 2) & self.rnMask) >> 5

    def getRDfield(self):
        return (int(self.instruction , 2) & self.rdMask) >> 0

    def checkShamt(self):
        return (self.opcode_field == "LSL" or self.opcode_field == "LSR" or self.opcode_field == "ASR")



    def getTranslation(self):

        self.getOpcode()

        if (self.opcode_field == "LSL" or self.opcode_field == "LSR" or self.opcode_field == "ASR" ):

            self.instruction_name = str(self.opcode_field) + "    R" + str(self.getRDfield()) +\
                                    ", R" + str(self.getRNField()) + ", #" + str(self.getShamtfield())

            return self.instruction_name

        else:
            self.instruction_name = str(self.opcode_field) + "    R" + str(self.getRDfield()) + ", R" +\
                                    str(self.getRNField()) + ", R" + str(self.getRMField())

            return self.instruction_name




