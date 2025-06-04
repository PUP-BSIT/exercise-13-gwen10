def miguel_profile():
    """Display Kian Miguel's profile information."""
    while True:
        print("\nGood day, everyone! I'm Kian Miguel, nice to meet you.")
        print("1. Basic Information About Kian")
        print("2. Kian's Goals")
        print("3. Teves Comment")
        print("4. Bataller Comment")
        print("5. Sario Comment")
        print("0. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        match choice:
            case "1":
                print("\nBasic Information About Kian")
                print("- 19 years old.")
                print("- From PUP Taguig.")
                print("- A 2nd year BSIT student.")
            case "2":
                print("\nKian's Goals")
                print("- To buy a McLaren and beat Max Verstappen in a race.")
                print("- To be called: Billionaire, Playboy, Philanthropist")
            case "3":
                print("\nTeves Comment")
                print("Okay, good luck with that!")
            case "4":
                print("\nBataller Comment")
                print("I believe you can achieve them!")
            case "5":
                print("\nSario Comment")
                print("You're making steady progress. Keep going!")
            case "0":
                print("\nReturning to Main Menu...")
                break
            case _:
                print("\nInvalid choice. Please try again.")
