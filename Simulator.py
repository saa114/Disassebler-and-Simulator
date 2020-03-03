import sys
import os
import BBreak
import Calculator
import RFormat
import Immediate
import IFormat
import IMFormat
import DFormat
import BFormat
import CBFormat
import Register

class Simulator(object):

    instruction_size = 100
    instruction = [None] * instruction_size
    instruction_count = 0
    executed_size = 50
    executed_instruction = [None] * executed_size
    execution_count = 0
    test = None
    outFile = None
    reg = None
    trans = ""
    byte = 96
    pc = 4
    bswitch = False
    cbswitch = False
    break_switch = False
    trans = ""

    def __init__(self , outFile , reg):

        self.outFile = outFile
        self.reg = reg

    def resize(self):
        
        temp = [0] * (self.instruction_size * 2)

        for i in range (0 , self.instruction_size):
            temp[i] = self.instruction[i]

        self.instruction = temp
        self.instruction_size = (self.instruction_size * 2)

    def addInstruction(self , row):

        self.instruction[self.instruction_count] = row
        self.instruction_count += 1


    def runSimulation(self):

        self.reg.resetRegistrs()

        for i in range(0, self.instruction_count + 1):

            calc = Calculator.Calculator(self.instruction[self.execution_count])

            if (self.break_switch == False):

                if (calc.getFormat() == "R"):
                    
                    self.test =  RFormat.RFormat(self.instruction[self.execution_count] , self.reg)
                    trans = self.test.getTranslation()


                elif (calc.getFormat() == "I"):

                    self.test = IFormat.IFormat(self.instruction[self.execution_count] , self.reg)
                    trans = self.test.getTranslation()

                elif (calc.getFormat() == "D"):

                    self.test = DFormat.DFormat(self.instruction[self.execution_count], self.reg)
                    trans = self.test.getTranslation()

                elif (calc.getFormat() == "B"):

                    self.test = BFormat.BFormat(self.instruction[self.execution_count])
                    trans = self.test.getTranslation()

                    if (self.test.getBRAdress() > 1):

                        if ((self.test.getBRAdress() + self.execution_count) > self.instruction_count):
                            print "Error: Branch is beyond Memory Space!!"
                            return

                        self.execution_count += (self.test.getBRAdress() - 1)

                    elif (self.test.getBRAdress() < 0 ):

                        if ((self.execution_count + self.test.getBRAdress()) < 0):
                            
                            print "Error: Branch is lower than Memory Space!! "
                            return

                        self.execution_count += (self.test.getBRAdress() - 1)
                    else:
                        None

                    self.bswitch = True

                elif (calc.getFormat() == "CB"):

                    self.test = CBFormat.CBFormat(self.instruction[self.execution_count], self.reg)
                    trans = self.test.getTranslation()

                    if (self.test.getBranch() > 1):

                       if ((self.test.getBranch() + self.execution_count) > self.instruction_count):
                            
                            print "Error: Branch is beyond Memory Space!! "
                            return

                       self.execution_count += (self.test.getBranch() - 1)

                    elif (self.test.getBranch() < 0):
                       if ((self.execution_count + self.test.getBranch()) < 0):
                            
                            print "Error: Branch is lower than Memory Space!! "
                            return

                       self.execution_count += (self.test.getBranch() - 1)
                    
                    else:
                        None

                    self.cbswitch = True

                elif (calc.getFormat() == "IM"):

                    self.test =  IMFormat.IMFormat(self.instruction[self.execution_count], self.reg)
                    trans = self.test.getTranslation()

                elif (calc.getFormat() == "Break"):

                    self.test = BBreak.BBreak(self.reg)
                    trans = self.test.getTranslation()
                    self.break_switch = True

                self.outFile.write("================================= \n"
                                      "cycle:" + str(i + 1) + " " + str(self.byte) + "  " + trans + "\n"
                                      "\n" +
                                       "Registers: \n" +
                                       "r00:    " + self.reg.returnRegisters(0, 8) + "\n" 
                                       "r08:    " + self.reg.returnRegisters(8, 16) + "\n"
                                       "r16:    " + self.reg.returnRegisters(16, 24) + "\n"
                                       "r24:    " + self.reg.returnRegisters(24, 32) + "\n \n"
                                       "data:   \n" + str(self.reg.printData()) + " \n")

            if (self.bswitch == False and self.cbswitch == False):
                 self.byte += 4
            
            else:
                self.branchByte()

            self.execution_count += 1


    def branchByte(self):

                if (self.bswitch == True) :
                    if (self.test.getBRAdress() > 1):
                        self.byte += (self.test.getBRAdress() * self.pc)

                    elif (self.test.getBRAdress() < 0 ):
                        self.byte -= (self.test.getBRAdress() * -self.pc)
                    
                    else:
                        self.byte += self.pc

                    self.bswitch = False

                elif (self.cbswitch == True):
                     if (self.test.getBranch() > 1):

                         self.byte += (self.test.getBranch() * self.pc)

                     elif (self.test.getBranch() < 0 ):

                        self.byte -= (self.test.getBranch() * -self.pc)
                     
                     else:
                        self.byte += self.pc

                     self.cbswitch = False

                else:
                     None
