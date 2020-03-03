# Disassebler-and-Simulator

This is a disassembler and simulator I created based on ARMv8 architecture.

############################# How to run ##############################################

    $python disassembler.py -i inputfile.txt -o outputname 

Where input inputfile.txt is a file that contains 32 bits of ARMv8 instructions.
outputname is any name you wish your output file to be called.

After running, 2 files will be generated:
outputname_dis.txt , which contains the disassebled program.
outputname_sim.txt , which containes the simulator for 


######################## Things to look out for ########################################

You can run your own inputfile, however keep these in mind:

1- The set of instructions in the inputfile must end with a break instruction, or else the program will not run.
Optional: You can have immediates after your break instruction. 

2- Branches that jump to an instruction beyond or before the number of instructionss available will print an error to the terminal screen and exit the program.

3- Loading(LDUR) from memory that has not been assigned yet will print an error and ignore the instruction. The program will still continue to execute.


