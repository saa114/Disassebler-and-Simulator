import Register

class IMFormat:

    OPCODE_LENGTH = 10
    INSTRUCTION_SIZE = 32
    instruction_name = 0
    opcode = ""
    opcode_feild = ""
    shift_field = 0
    data_field = 0
    rd_field = 0
    rdMask = 0x1F
    imsftMask = 0x600000
    imdataMask = 0x1FFFE0
    instruction = ""
    _reg = None


    def __init__(self , MyList , reg):

       for x in range(0 , self.INSTRUCTION_SIZE - 1):
            self.instruction = ''.join(str(e) for e in MyList)

       self._reg = reg

    def getOpcode(self,  *args ):

       self.opcode = self.instruction[0:11]
       self.opcode = int(self.opcode , 2)

       if (self.opcode >= 1684 and self.opcode <= 1687 ):

            self.opcode_feild = "MOVZ"
            self._reg.addMOVZ(self.getRDFeild() , self.getDataField() , self.getShiftField())

            return self.opcode_feild

       elif (self.opcode >= 1940 and self.opcode <=1943):

            self.opcode_feild = "MOVK"
            self._reg.addMOVK(self.getRDFeild() , self.getDataField() , self.getShiftField())

            return self.opcode_feild
       
       else:
           pass

    def getDataField(self):
        
        self.data_field = (int(self.instruction , 2) & self.imdataMask) >> 5
        return self.data_field


    def getRDFeild(self):
        
        self.rd_field = (int(self.instruction , 2) & self.rdMask) >> 0
        return self.rd_field

    def  getShiftField(self):
        
        self.shift_field = (int(self.instruction , 2) & self.imsftMask) >> 17
        return self.shift_field

    def getTranslation(self):
       
        self.instruction_name = str(self.getOpcode()) + "   " + "R" + str(self.getRDFeild()) +\
                               "," + " "+ str(self.getDataField()) + " " + "LSL " + \
                               " " + str(self.getShiftField())
       
        return self.instruction_name





