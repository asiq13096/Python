weight = input("Enter your weight: ")
conv = input(f'(L)bs or (K)g: ')
if conv == 'L' or conv == 'l':
    print("you are " + str(0.45*float(weight)) + " pounds")
elif conv == 'K' or conv == 'k':
    print("you are " + str(2.20*float(weight)) + " kilos")