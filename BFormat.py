class BFormat:

    OPCODE_LENGTH = 10
    INSTRUCTION_LENGTH = 32
    instruction_name = ""
    opcode = ""
    opcode_feild = ""
    br_adress = ""
    brMask = 0x3FFFFFF
    instruction = ""
    _reg = None
    branch = 0

    def __init__(self , MyList):

       for x in range(0 , self.INSTRUCTION_LENGTH - 1):
            self.instruction = ''.join(str(e) for e in MyList)

    def getOpcode(self,  *args ):

       self.opcode = self.instruction[0:11]
       self.opcode = int(self.opcode , 2)

       if (self.opcode >= 160 and self.opcode <= 191):
            self.opcode_feild = "B"
            return self.opcode_feild

    def getBRAdress(self):

        if (self.instruction[6] == "1"):

            self.br_adress = ""
            for i in range(0 , len(self.instruction)) :

                    if (self.instruction[i] == "1"):
                        self.br_adress += "0"
                    else:
                        self.br_adress += "1"

            self.br_adress = int(self.br_adress, 2)
            self.br_adress = self.br_adress & self.brMask
            self.br_adress += 1

            return (self.br_adress * -1)

        else:

            self.br_adress = self.instruction
            self.br_adress = int(self.br_adress , 2)
            self.br_adress = self.br_adress & self.brMask

            return self.br_adress

    def getTranslation(self):
        
        self.instruction_name = str(self.getOpcode()) + "   #" + str(self.getBRAdress())
        return self.instruction_name

