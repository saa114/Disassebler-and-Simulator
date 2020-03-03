class CBFormat:

    OPCODE_LENGTH = 10
    INSTRUCTION_LENGTH = 32
    instruction_name = ""
    opcode = ""
    opcode_feild = ""
    cbr_adress = 0
    cbrMask = 0xFFFFE0
    rtMask = 0x1F
    instruction = ""
    _reg = None
    branch = 0


    def __init__(self , MyList , reg):

       for x in range(0 , self.INSTRUCTION_LENGTH - 1):
            self.instruction = ''.join(str(e) for e in MyList)

       self._reg = reg


    def getOpcode(self,  *args ):

       self.opcode = self.instruction[0:11]
       self.opcode = int(self.opcode , 2)

       if (self.opcode >= 1440 and self.opcode <= 1447):
            
            self.opcode_feild = "CBZ "
            self.branch = self._reg.cbzAddress(self.getRTFeild() , self.getCBRAdress())

            return self.opcode_feild

       elif (self.opcode >=  1448 and self.opcode <= 1455):
            
            self.opcode_feild = "CBNZ"
            self.branch = self._reg.cbnzAddress(self.getRTFeild() , self.getCBRAdress())
            
            return self.opcode_feild
       
       else:
           pass

    def getCBRAdress(self):

        self.cbr_adress = ""

        if (self.instruction[8] == "1"):

            for i in range(0 , len(self.instruction)) :

                    if (self.instruction[i] == "1"):
                        self.cbr_adress += "0"

                    else:
                        self.cbr_adress += "1"


            return  -(((int(self.cbr_adress, 2) & self.cbrMask) >> 5)  + 1)

        else:

            return (int(self.instruction, 2) & self.cbrMask) >> 5

    def getRTFeild(self):
        return (int(self.instruction , 2) & self.rtMask) >> 0

    def getBranch(self):
        return self.branch


    def getTranslation(self):

        self.instruction_name = str(self.getOpcode()) + "   R" + str(self.getRTFeild()) \
                                + "," + " #" + str(self.getCBRAdress())
        return self.instruction_name
