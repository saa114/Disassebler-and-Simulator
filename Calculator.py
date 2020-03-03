class Calculator(object):

    opcode = 0
    instruction =""
    OPCODE_LENGTH = 10
    format = ''
    bbreak = False
    INSTRUCTION_SIZE = 32
    instruction_set = [0] * 32

    def __init__(self , MyList  , *args):

          self.instruction = MyList

    def getOpcode(self):

        self.opcode = self.instruction[0:11]
        self.opcode = int(self.opcode, 2)

        return self.opcode

    def getFormat(self):
        
        self.getOpcode()

        if (self.bbreak == False):

           if (self.opcode == 0):
               
               self.format = "R"
               return self.format

           elif(self.opcode >= 160 and self.opcode <= 191):

               self.format = "B"
               return self.format

           elif (self.opcode >= 1160 and self.opcode <= 1161):

               self.format = "I"
               return self.format

           elif (self.opcode >= 1440 and self.opcode <= 1447):
               
               self.format =  "CB"
               return self.format
           
           elif (self.opcode >= 1448 and self.opcode <= 1455):
               
               self.format =  "CB"
               return self.format
           
           elif (self.opcode >= 1672 and self.opcode <= 1673):
               
               self.format =  "I"
               return self.format

           elif (self.opcode >= 1684 and self.opcode <= 1687):
           
               self.format =  "IM"
               return self.format

           elif (self.opcode >= 1940 and self.opcode <= 1943):
               
               self.format =  "IM"
               return self.format

           elif (self.opcode == 1104):
           
               self.format = "R"
               return self.format

           elif (self.opcode == 1112):
               
               self.format = "R"
               return self.format

           elif (self.opcode == 1360):
               
               self.format = "R"
               return self.format

           elif (self.opcode == 1872):
               
               self.format = "R"
               return self.format

           elif (self.opcode == 1624):
           
               self.format = "R"
               return self.format

           elif (self.opcode == 1690):
               
               self.format = "R"
               return self.format

           elif (self.opcode == 1691):
               
               self.format = "R"
               return self.format

           elif (self.opcode == 1692):
               
               self.format = "R"
               return self.format

           elif (self.opcode == 1360):
           
               self.format = "R"
               return self.format

           elif (self.opcode == 1984):
           
               self.format = "D"
               return self.format

           elif (self.opcode == 1986):
               
               self.format = "D"
               return self.format

           elif (self.opcode == 1616):
           
               self.format = "R"
               return self.format

           elif (self.opcode == 2038):
           
               self.format = "Break"
               return self.format

           else:
               pass
        else:
               pass















