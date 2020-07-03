condition = ""
while condition != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car started.....")
    elif command == "stop":
        print("Car stoped.....")
    elif command == "quit":
        print("""
        start - for starting car
        stop - for stopping the car
        quit - to quit the game
        """)
    else:
        print("sorry!! I cann't understand you!!!")