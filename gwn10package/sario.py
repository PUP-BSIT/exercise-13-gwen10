def sario_profile():
    """ Display Gerald Sario's profile information. """
    while True:
        print("\nGood day, everyone! I'm Gerald Sario, nice to meet you!")
        print("\n1. Basic Information about Gerald")
        print("2. My Goals")
        print("3. Teves Comment")
        print("4. Bataller Comment")
        print("5. Gonato Comment")
        print("6. Miguel Comment")
        print("0. Back to Team Menu")

        choice = input("\nEnter your choice: ").strip()

        match choice:
            case "1":
                print("\nHello Everyone! I'm Gerald Sario.")
                print("- 20 years old.")
                print("- Studying in PUP - Taguig")
                print("- 2nd year student of BSIT")
            case "2":
              print("My goal is to be rich, richer, and richest.")
              print("Become a millionaire, billionaire, and trillionaire.")
            case "3":
                print("\nTeves Comment")
                print("Keep reaching for your dreams, Gerald!")
            case "4":
                print("\nBataller Comment")
                print("Your positivity is contagious, Gerald! Keep it up!")
            case "5":
                print("\nGonato Comment")
                print("Great job! Just a few tweaks and this is solid.")
            case "6":
                print("\nMiguel Comment")
                print("Goodluck on your goals, I hope you achieve it!")
            case "0":
                print("\nReturning to Main Menu...")
                break
            case _:
                print("\nInvalid option. Please try again.")