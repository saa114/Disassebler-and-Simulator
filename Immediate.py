class Immediate(object):

    INSTRUCTION_LENGTH = 32
    instruction = [] * 32
    immediate = 0
    _reg = None
    byte = 0


    def __init__(self , MyList , reg , byte):

       self.instruction = list(MyList)
       self._reg = reg
       self.byte = byte

       for i in range(len(self.instruction)):
           self.instruction[i] = int(self.instruction[i])

    def getTranslation(self):

       for x in range(0, self.INSTRUCTION_LENGTH - 1):

           if (x == 0 and self.instruction[x] == 0):
               
               self.immediate = self.instruction[x]
               self.immediate *= 2
               self.immediate += self.instruction[x + 1]

           elif(x == 0 and self.instruction[x] == 1):
               
               self.immediate = self.instruction[x]
               self.immediate *= (-2)
               self.immediate += self.instruction[x + 1]

           elif (x < self.INSTRUCTION_LENGTH ):
               
               self.immediate *= 2
               self.immediate += self.instruction[x + 1]

           else:
               pass

       self._reg.addData(self.immediate, self.byte)

       return str(self.immediate)
     

