def bataller_profile():
    """Display Christian Bataller's profile information."""
    while True:
        print("\nHello, everyone! I'm Christian Bataller, Have a great day!")
        print("1. Basic Information About Christian")
        print("2. Christian's Goals")
        print("3. Teves Comment")
        print("4. Sario Comment")
        print("5. Gonato Comment")
        print("6. Miguel Comment")
        print("0. Back to Main Menu")
        
        choice = input("\nEnter your choice: ").strip()
        
        match choice:
            case "1":
                print("\nBasic Information about Christian")
                print("Province: Bicol")
                print("I love singing, cooking, and travelling.")
            case "2":
                print("\nBataller Goals")
                print("- To achieve what I am currently pursuing.")
                print("- To give my whole support to my family in future.")
            case "3":
                print("\nTeves Comment")
                print("Keep up the good work and stay positive!")
            case "4":
                print("\nSario Comment")
                print("Clear and readable. Nice job!")
            case "5":
                print("\nGonato Comment")
                print("Awesome work! Very readable and entertaining.")
            case "6":
                print("\nMiguel Comment")
                print("Goodluck to your dream. Soar high!")
            case "0":
                print("\nReturning to Main Menu...")
                break
            case _:
                print("\nInvalid choice. Please try again.")