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
import Simulator

class Dissasembler:

    def main():

      col = 32
      bbreak = False
      translation = None
      inputFileName = ""
      outputFileName =""
      instructions = ""
      switch = False
      switch2 = False
      byte = 96
      cycle = 1;
      trans = ""


      for i in range(len(sys.argv)):   #The code that gets the file name from the command line
          if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
              inputFileName = sys.argv[i + 1]
          elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
              outputFileName = sys.argv[i + 1]


      instructions = [line.rstrip() for line in open(inputFileName, 'rb')]
      outFile = open(outputFileName + "_dis.txt", 'w')#The code that writes the lines into the file
      outFile2 = open(outputFileName + "_sim.txt", 'w')
      reg = Register.Register()
      simulator = Simulator.Simulator(outFile2 , reg)


      with open(outputFileName, 'a') as k:

                 for i in range(0, len(instructions)):

                    row = ""
                    row += instructions[i]

                    simulator.addInstruction(row)
                    
                    if (bbreak == False):

                        calc = Calculator.Calculator(row)

                        if (calc.getFormat() == "R"):
                            translation = RFormat.RFormat(row , reg)

                        elif (calc.getFormat() == "I"):
                            translation = IFormat.IFormat(row , reg)

                        elif (calc.getFormat() == "D"):
                            translation = DFormat.DFormat(row, reg)

                        elif (calc.getFormat() == "B"):
                            translation = BFormat.BFormat(row)

                        elif (calc.getFormat() == "CB"):
                            translation = CBFormat.CBFormat(row, reg)

                        elif (calc.getFormat() == "IM"):
                            translation = IMFormat.IMFormat(row, reg)

                        elif (calc.getFormat() == "Break"):

                            bbreak = True
                            translation = BBreak.BBreak(reg)

                    elif (bbreak == True):

                            switch = True
                            translation = Immediate.Immediate(row , reg , byte)
                    else:
                         pass
                    trans = translation.getTranslation()


           #this part of the loop that writes into the destined file from the first line to last line
           # if instruction is R /// just for example but will read in file and use appropriate spacings just remove hard code
                    if (switch == False ):
                       j = 0
                       while j < col:
                           
                           outFile.write(instructions[i][j])
                           
                           if (j == 7 or j > 7 and j < 30 and j % 5 == 0):
                               outFile.write(" ")
                           
                           j = j + 1
                       
                       outFile.write("  " + str(byte).center(4) + "  " + trans + "\n")

                    else:
                        
                         j = 0
                         while j < col:

                             outFile.write(instructions[i][j])
                             j = j + 1
                             
                         outFile.write(" " + str(byte) + " " + '%-10s'  '%s' % (trans, ' ') + "\n")



                    byte += 4
                    cycle += 1

      k.close()
      outFile.close()

      simulator.runSimulation()

    if __name__== "__main__":
         main()
