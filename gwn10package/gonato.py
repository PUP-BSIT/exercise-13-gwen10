def gonato_profile():
    """ Display Alexa Gonato's profile information. """
    while True:
        print("\n=== Hi! Welcome to Jan Alexa Louisse P. Gonato's Menu ===")
        print("[1] Alexa's Basic Info")
        print("[2] Alexa's Goals")
        print("[3] Teves Comment")
        print("[4] Bataller Comment")
        print("[5] Sario Comment")
        print("[0] Return to Main Menu")

        choice = input("Please enter your choice: ").strip()

        match choice:
            case "1":
                print("\nAlexa's Basic Info")
                print("I am an IT student from BSIT 2-1.")
            case "2":
                print("\nAlexa's Goals")
                print("To finally stop saying ‘student p lng’ in every intro.")
            case "3":
                print("\nTeves Comment")    
                print("Good luck with your dream! I know you can do it!")
            case "4":
                print("\nBataller Comment")
                print("Your determination is inspiring!")
            case "5":
                print("\nSario Comment")
                print("You're doing a great job. Keep it up!")
            case "0":
                print("\nReturning to Main Menu")
                print("Goodbye champ! PEACE OUT!")
                break
            case _:
                print("\nInvalid choice. Please try again.")