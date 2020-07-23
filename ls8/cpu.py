"""CPU functionality."""

import sys

LDI = 0b10000010
HLT = 0b00000001
PRN = 0b01000111
MUL = 0b10100010
NOP = 0b00000000
POP = 0b01000110
RET = 0b00010001 # opcode 10
CALL = 0b01010000 # opcode 9 
PUSH = 0b01000101
SP = 0b00000111
ADD = 0b10100000
PUSH = 0b01000101
POP = 0b01000110



# Why is it called LS8? 
# 8 Bit Instruction Set
# Because we have 256 bytes of memory, from our CPU we have the memory bus that will go out to RAM,
# If we have 8 bytes, we have 8 of them(bus) These Bus wires tell the RAM where to go
class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Why can't the LS8 have more ram? (memory)
        # A: Becuase of our 8 bit bus, our CPU has to communicate with RAM
        # In order to do that we've set our CPU up with a bunch of wires connecting to RAM (Data Bus, Memory Bus, System Bus, Address Bus)
        # We use our Data bus ()
        self.ram = [0] * 256 # 255 bytes or in /hex FF
        self.reg = [0] * 8 # 8 Registers, LS8 8 Bit Instruction
        self.flag = 0
        self.pc = 0 # program counter
        self.running = True 
        self.SP = 0b00000111
     
        

        
    # Load the program into memory 
    # Un-hardcode the machine code
    # Implement the load() function to load an .ls8 file given the filename passed in as an argument
    def load(self):
        """Load a program into memory."""
        
        # Note that sys.argv[0] is the name of the running program itself.
        # so you can look in sys.argv[1] for the name of the file to load
        filename = sys.argv[1]
        address = 0 # number command, index 

        with open(filename) as f:
            for line in f:
                line = line.split('#')[0].strip()
                if line == '':
                    continue
                try:
                    v = int(line, 2) # instruction 
                except ValueError:
                    continue
                self.ram_write(address, v)
                address += 1 # Increment after we load it up 


    # Instructions 
    # implement the HLT instruction handler
    # exit the loop if a HLT instruction is encountered
    def HLT(self, reg_a, reg_b):
        self.running = False

    # Set the value of a register to an integer
    # This instruction sets a specified register to a specified value.
    # How does it know which value? 
    # How does it know which register? 
    def LDI(self, reg_a, reg_b):
        self.reg[reg_a] = reg_b


    # Print numeric value stored in the given register
    def PRN(self, reg_a, reg_b):
        print(self.reg[reg_a])

    # Implement a Multiply instruction
    # This is an instruction handled by the ALU
    def MUL(self, reg_a, reg_b):

        self.alu("MUL", reg_a, reg_b)

     # Implementing the stack to PUSH & POP Registers using a pointer to memory in our stack  
    def PUSH(self, reg_a, reg_b): # take in the comparsion values (registers)
        # how do we know which reg num? its opperand a 
         reg_num = self.ram[reg_a] # add register a to ram, go into memory & get value  
         # value is found in a given register 
         value = self.reg[reg_num] # Add Ram value to register, get value to add to stack pointer address
         # Register 7 is for the Stack Pointer
         self.reg[SP] -= 1 # When we push we decrement our stack pointer (SP). Stack Pointer is stored in a register
         top_of_stack_add = self.reg[SP]
         self.ram[top_of_stack_add] = value # Add value to top of stack. Memory at the Stack Pointer = the value

   # NO OP means dont do anything 

    def POP(self, reg_a, reg_b):
        # POP is a 2 BYTE command
        # Pop whatever was last pushed to stack 
        
        # Get the Stack Pointer
        top_of_stack_add = self.reg[SP] # get/add the Stack Pointer value to the register 

        # Get the Register number 
        value = self.ram[top_of_stack_add] # Get the vaalue at top of stack 
        # register number is in our memory at opperand a 
        reg_num = self.ram[reg_a] # Create ram storage for reg_a. Get register number to put the value in 

        # Put value into given Register 
        self.reg[reg_num] = value # put the value into the given register 

        # Increment Stack Pointer
        self.reg[SP] += 1    # Move Stack Pointer Up, increment SP is stored in register 7 


    
    # ALU Math Operations 
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
             self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

        ## Step 2: Add RAM functions

    # implement the core of run 
    # This is the workhorse function of the entire processor
    # It needs to read the memory address that's stored in register PC, 
    # and store that result in IR, the Instruction Register.
    def run2(self):
        # Pull out each command as we go 
        
        
        
        while self.running:
           # lets use a pointer into the array (Program Counter) count where we our in the execution of the program
           command = self.ram[self.pc] # our command in the program is wherever that counter is pointing

           operand_a = self.ram_read(self.pc + 1) # Place Counter value 1
           operand_b = self.ram_read(self.pc + 2) # Place Counter value 2

           # Set the value of a register to an integer.
           if command == LDI:
               self.reg[operand_a] = operand_b
               self.pc += 3
           # Print numeric value stored in the given register.   
           elif command == PRN: # this operation is 2 bytes 
               print(self.reg[operand_a])
               self.pc += 2    
           elif command == MUL:
               print("MULLIGAN")
               print(operand_a)
               print(operand_b)
               # Multiply the values in two registers together and store the result in registerA.
               self.reg[operand_a] = self.reg[operand_a] * self.reg[operand_b]    
               # Increment place counter else infinite loop   
               self.pc += 3
           elif command == ADD:
                operand_a = self.ram_read(self.pc + 1)
                operand_b = self.ram_read(self.pc + 2)
                self.reg[operand_a] = self.reg[operand_a] + self.reg[operand_b]
                self.pc += 3

           elif command == PUSH:
                 # print("PUSHIN")
                 # get the register number
                 # operand_a = self.ram_read(self.pc + 1)
                 operand_a = operand_a #Register whose value is to be pushed on stack
                 
                 # Write to Ram the Stack Pointer (R7) & operand_a
                 self.ram_write(self.SP, self.reg[operand_a]) 

                 self.pc += 2 # Increment by 2 because this is a 2 byte operation

                 # decrement the stack pointer
                 self.SP -= 1
                # print(self.SP)

           elif command == POP:
               operand_a = self.ram_read(self.pc + 1)  # Register in which stack value is to be popped
               self.reg[operand_a] = self.ram_read(self.SP+1)
               self.SP += 1
               self.pc += 2
           elif command == CALL: # Calls a subrotuine(function) at the address stored in register 
               # The PC is set to the address in the given register, we then JUMP to that location in RAM
               # How to pass parameters when we CALL? 
               # Where do we store the Data? (Register: will get overwrite so we use the Stack)
               # IF WE CALL ---- WE HAVE TO RET (Return)
               #print("CALLIN")
               # get register number
               operand_a = self.ram_read(self.pc + 1) # operan_a = reg
               

               # Figure out the address of our subroutine 
               # Put that address into a register 
               # get the address to jump to from the register
               address = self.reg[operand_a]

               # push command after CALL on the Stack (we use stacks because register might be overwritten in subroutine)
               return_address = self.pc + 2 # IF this = 2 then the PC is 8, is that correct?
               # You want this to be 8

               #print(self.pc, self.pc) # 6
               # Save where we're going back to 

               # decrement stack pointer 
               # write the value to the memory address that the stack pointer is at
               self.SP -= 1
               self.ram_write(self.SP, self.pc + 2)
               
               sp = self.SP
               #print(sp, sp) # 6
               # put the address on the stack
               self.ram[sp] = return_address
               #print(return_address, return_address) # 7

               # then look at register, jump to that address 
               # Run whatever commands are there 
               self.pc = address
               #print(address, address) # 24

            # RET (POP OFF THE STACK & JUMP) We JUMP back so we don't hit HALT & so we can continue program execution
            # RET will POP the return address off of the stack & store it in PC   
           elif command == RET:
               #print("RETTIN")
               # pop the return address off the stack 
               sp = self.SP # R7
               self.SP += 1
               return_address = self.ram[sp] 
              # print(self.ram[sp])
              # print(self.reg)
              # go to return address: set PC to return address 

               self.pc = return_address 
               # print(self.pc, self.pc) 
                



                


           elif command == HLT:
               sys.exit(0)
           else:
                print(f"Run2 Did Not Work")
                sys.exit(1) 

    # Research Turing Complete 
           

    # access the RAM inside the CPU object.

    def ram_read(self, address):
         return self.ram[address]

    def ram_write(self, address, value):
         self.ram[address] = value
