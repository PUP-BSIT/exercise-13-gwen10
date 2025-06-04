def teves_profile():
    """ Display Gwen Teves' profile information. """
    while True:
        print("\nGood day, everyone! I'm Gwen Teves, nice to meet you!")        
        print("\n1. Basic Information About Gwen")
        print("2. Gwen's Goals")
        print("3. Bataller Comment")
        print("4. Sario Comment")
        print("5. Gonato Comment")
        print("0. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()
        
        match choice:
            case "1":
                print("\nBasic Informations About Gwen")
                print("- 19 yrs old.")
                print("- From PUP Taguig.")
                print("- A 2nd year BSIT student.")
            case "2":
                print("\nGwen's Goals")
                print("- To graduate on time and live peacefully.")
                print("- To become an expert programmer.")
            case "3":
                print("\nBataller Comment")
                print("Keep fighting, Gwen! You're doing great!")
            case "4":
                print("\nSario Comment")
                print("You’re getting better every time. Keep going!")
            case "5":
                ("\nGonato Comment")
                print("You’re getting better every time. Keep going!")
            case "0":
                print("\nReturning to Main Menu...")
                break
            case _:
                print("\nInvalid choice. Please try again.")

