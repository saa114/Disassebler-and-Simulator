class DFormat:

    OPCODE_LENGTH = 10
    INSTRUCTION_SIZE = 32
    instruction_name = ""
    opcode = ""
    opcode_feild = ""
    dt_adress =0
    rn_field = 0
    rt_field = 0
    op_field = 0
    rnMask = 0x3E0
    rtMask = 0x1F
    opMask = 0xC00
    dtMask = 0xFF000
    instruction = ""
    _reg = None

    def __init__(self , MyList , reg):

       for x in range(0 , self.INSTRUCTION_SIZE - 1):
            self.instruction = ''.join(str(e) for e in MyList)

       self._reg = reg

    def getOpcode(self):

       self.opcode = self.instruction[0:11]
       self.opcode = int(self.opcode, 2)

       if (self.opcode == 1984 ):

            self.opcode_feild = "STUR"
            self._reg.sturAddress(self.getRTFeild() , self.getRNField(), self.getDTAdress())
            
            return self.opcode_feild

       elif (self.opcode == 1986):

            self.opcode_feild = "LDUR"
            self._reg.ldurAddress(self.getRTFeild() , self.getRNField(), self.getDTAdress())
            
            return self.opcode_feild
       else:
           pass

    def getDTAdress(self):
        return (int(self.instruction , 2) & self.dtMask) >> 12


    def getOP(self):
        return (int(self.instruction , 2) & self.opMask) >> 10


    def getRNField(self):
        return (int(self.instruction , 2) & self.rnMask) >> 5


    def getRTFeild(self):
        return (int(self.instruction , 2) & self.rtMask) >> 0


    def getTranslation(self):

       self.instruction_name = str(self.getOpcode()) + "   R" + str(self.getRTFeild()) +\
                               "," + " " + "[R" + str(self.getRNField()) + "," + " " + "#" +\
                                str(self.getDTAdress()) + "]"

       return self.instruction_name




