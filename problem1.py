side_1 = int(input("Please enter the value of side 1: "))
side_2 = int(input("Please enter the value of side 2: "))
side_3 = int(input("Please enter the value of side 3: "))

square_1 = side_1**2
square_2 = side_2**2
square_3 = side_3**2

if (square_1+square_2 == square_3) or (square_1+square_3 == square_2) or (square_2+square_3 == square_1):
    print("A triangle with lengths " + str(side_1) + ", " +
    str(side_2) + ", and " + str(side_3) + " forms a right-angled triangle.")
else:
    print("A triangle with lengths " + str(side_1) + ", " +
    str(side_2) + ", and " + str(side_3) + " does not form a right-angled triangle.")




