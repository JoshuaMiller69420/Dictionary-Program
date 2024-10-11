acronyms = {"BRB": "Be Right Back", 
            "LOL": "Laugh Out Loud", 
            "LMAO": "Laugh My Astronaut Of", 
            "AFK": "Away From Keyboard", 
            "TY": "Thank You"
            } 


for key in acronyms:
    print(key, acronyms[key])

print(acronyms.items())
for key, value in acronyms.items():
    print(f"{key}: {value}")



# Example dictionary
my_dict = {"BRB": "Be Right Back", 
            "LOL": "Laugh Out Loud", 
            "LMAO": "Laugh My Astronaut Of", 
            "AFK": "Away From Keyboard", 
            "TY": "Thank You"
            } 

# Append a new key-value pair using dict() constructor
user_in1 = input("Enter a acronym you want to add to the dictionary: ").upper()
user_in2 = input("Enter a acronym you want to add to the dictionary: ").lower()
my_dict[user_in1] = user_in2

print(my_dict)