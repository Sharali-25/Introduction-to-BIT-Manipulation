n = int(input("Enter a number (5 or 12)"))
guess = input("Guess its binary ") 
input("Binary press enter") 
print("Decimal = decimal ",n,"Binary = ",bin(n)[2:])
print("Your guess was ",guess)

# BIT wise not, xor,left shift,right,shift,and, or

n= int(input("Enter a number"))
print("not of 12 is " ,~12)
print("25 xor 7 is ", 25^7)
print("left shift of " , n ,"=",n<<1)
print("Right shift of " , n,"=", n>>1)
print("35 and 12 ", 35&12)
print("45 or 15 ", 45|15)