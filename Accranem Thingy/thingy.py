acronyms = {"BRB": "be right back", 
            "LOL": "laugh out loud", 
            "LMAO": "laugh my astronaut of", 
            "AFK": "away from keyboard", 
            "TY": "thank you"
            } 


def acro_accesser() -> None:
    user_in = input("Enter an acronym (enter Q to quit): ").upper()
    if user_in == "Q":
        return
    elif user_in == "LOL":
        x = acronyms.get("LOL")
        print(x)
    elif user_in == "BRB":
        x = acronyms.get("BRB")
        print(x)
    elif user_in == "LMAO":
        x = acronyms.get("LMAO")
        print(x)
    elif user_in == "AFK":
        x = acronyms.get("AFK")
        print(x)
    elif user_in == "TY":
        x = acronyms.get("TY")
        print(x)
    else:
        print("Acronym dose not exist.")


def add_acro(acronyms) -> None:
    user_in1 = input("Enter a acronym you want to add to the dictionary: ").upper()
    user_in2 = input("Enter a discription for you acronym: ").lower()
    acronyms[user_in1] = user_in2
    print(f"Acronym {user_in1} was added.")


def acro_list() -> None:
    print(acronyms)


def play_game():
    while True:
        print("Would you like to look at acronyms or add some?")
        print("1. Look up acronyms.")
        print("2. Add an acronym.")
        print("3. List of acronyms with discription.")
        print("4. Exit.")
        user_choice = input("Enter your choice (1-4): ")
        
        if user_choice == "1":
            acro_accesser()
        elif user_choice == "2":
            add_acro(acronyms)
        elif user_choice == "3":
            acro_list()
        elif user_choice == "4":
            exit()


if __name__ == '__main__':
    play_game()
