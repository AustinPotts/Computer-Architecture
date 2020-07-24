

import sys 
print(sys.argv)

# How do we read a file in Python?
with open("print8.ls8") as file:
    for line in file:
        split_line = line.split('#')
        commad = split_line[0].strip()

        print(line)
        print(split_line)
        print(commad)




  # implement the core of run 
    # This is the workhorse function of the entire processor
    # It needs to read the memory address that's stored in register PC, 
    # and store that result in IR, the Instruction Register.
    def run(self):
         while self.running: # while we are running 
             # Instruction Reader = the place counter in Ram pointing at instruction 
             ir = self.ram_read(self.pc)  # read memory address and store in IR Instruction Register
             pc_flag = (ir & 0b00010000) >> 4 # shift right, checking for 1 in spot 
             reg_num1 = self.ram[self.pc +1] # Using ram_read(), read the bytes at PC+1 and PC+2 from RAM into variables operand_a and operand_b
             reg_num2 = self.ram[self.pc + 2]
             self.branch_table[ir](reg_num1, reg_num2) # Run instruction 
             if pc_flag == 0:
                 move = int((ir & 0b11000000) >>6) # shift right 6 places checking for 1 spot
                 self.pc += move + 1 # After running code for any particular instruction, the PC needs to be updated
                                     # to point to the next instruction for the next iteration of the loop in run()       