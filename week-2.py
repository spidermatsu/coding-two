#Write a program in python that will take a value and display it in its binary form 
# using only what's available in the default python environment (ie. no external packages).

base2_array = [128, 64, 32, 16, 8, 4, 2, 1]
num = 0
output = ""
print("binary to denary converter")

try:
    num = int(input("Type a number less than 255: "))
except ValueError:
    print("Not a number")
    quit()

if num > 255:
    print("too big, try again")
    quit()
else:
    pass

for i in base2_array:
    if (num - i) >= 0:
        output += '1' 
        num -= i
    else:
        output += '0'

print(output)