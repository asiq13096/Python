name = input("Enter your name: ")
if len(name)<3:
    print("Name must be at least 3 characters's!!!")
elif len(name)>10:
    print("Name can be a maximum of 10 character's!!!")
else:
    print("Name looks good.")