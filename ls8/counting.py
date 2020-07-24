
# Number Symbols


# Decimal len(10)
# Base 10

0-9 
1 
2
3
...
9
10

20 
30
40
...
99
100


# Hexadecimal
# What symbols do we have in hex? (16)
# Base 16
0
...
9
A # 10
B # 11
C # 12
D # 13
E # 14
F # 15
# Now we're out of symbols. Whats 16?
# We turn the F into a 0 & bump it over 
10 # 16 or 0x10
11 # 17 
12 # 18
13 # 19 
14 # 20 
15 # 21
16 # 22 
17 # 23 
18 # 24 
19 # 25
1A # 26
1B # 27 
1C # 28 
1D # 29 
1E # 30 
1F # 31
20 # 32


#Binary 
01 

0 # 0
1 # 1
# turn 1 into 0  & bump over 
10 # 2
11 # 3
100 # 4 
101 # 5
110 # 6
111 # 7
# out of slots 
1000 # 8 
1001 # 9
1010 # 10 
1011 # 11
1111 # 12


# Hexadeciaml to Decimal 

# How many times have you looped through 16
# 0x always means Base 16
# 0b means decimal 
# I.E 0x10 = 16 
# 0x20 = 32
# 0x30 = 48
# 0x40 = 64

# this number times 16
(7 * 16) + 3 = .... 112 + 3 = 115
0x73



0x3F
# The 3 here means we looped through our symbols 3 times 
(3 * 16) + 15 = ... 48 + 15 = 63


# Convert the Decimal to Hexadecimal 
# Devide by 16 
54 

(54 / 16) = 3.??
# 3 times 16 is 48
54 - 48 = 6 
0x36


# Convert 
0xE3

(14 * 16) + 3 = ... 224 + 3 = 227


# Binary to Decimal 
0b11001010
        ^ # 1 in the 2's place
       ^ # 1 in the 8's place ( we double as we go )
    ^ # 1 in the 64's place
   ^ # 1 in the 128 place 
# Go right to left 
2 + 8 + 64 + 128 = 202


# Binary to Hexadecimal 
# one trick is to do it in halves I.E 0b1010 1100
# 0b1010 # First Half 
      ^ # 1 in 2's place 
    ^ # 1 in 8's place
2 + 8 = 10 # 10 Hexadecimal is A 

# 1100 # Second Half 
   ^ # 1 in 4's place 
  ^ # 1 in 8's place 
4 + 8 = 12  # 12 Hexadecimal is C

0b10101100 # we have 8 binary bits here (byte) 4 = (nibble)
 0xAC # Converted to hexadeciaml 
# 0b1010 1100
    


# 1
# 11
# 111 
# 0b1111 = F


# Hexadecimal to decimal 
0xAC 
(10 * 16) + 12 = 172

# Decimal to Hex to Binary & The Other Way Around 

0b11111111

# Break it in 1/2
# 0b1111 
       ^ # 1 in 1's place 
      ^ # 1 in 2's place 
     ^ # 1 in the 4's place 
    ^ # 1 in the 8's place 
1 + 2 + 4 + 8 = 15 

# 1111
# Same amount, we have 15 
1 + 2 + 4 + 8 = 15 
0xFF

