# Write your code to expect a terminal of 80 characters wide and 24 rows high


import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('LordOfTheRings')

auth_sheet = SHEET.worksheet('Auth')
quiz_sheet = SHEET.worksheet('Quiz')


# Function to register a new user
def register(username, password):
    try:
        # Check if username already exists
        usernames = auth_sheet.col_values(1)
        if username in usernames:
            print("Username already exists. Please choose a different username.")
            return False

        # Add new user to the 'Auth' worksheet
        auth_sheet.append_row([username, password])
        print("Registration successful. You can now log in.")
        return True
    except Exception as e:
        print(f"Error during registration: {e}")
        return False

# Function to authenticate a user
def login(username, password):
    try:
        # Find the row corresponding to the username
        usernames = auth_sheet.col_values(1)
        if username not in usernames:
            print("Username not found. Please register first.")
            return False

        index = usernames.index(username) + 1  # Adding 1 because indexing starts from 1 in Google Sheets
        stored_password = auth_sheet.cell(index, 2).value

        # Check if the provided password matches the stored password
        if password == stored_password:
            print("Login successful.")
            return True
        else:
            print("Incorrect password.")
            return False
    except Exception as e:
        print(f"Error during login: {e}")
        return False
    

    # Function to check if a user exists
def check_user(username):
    try:
        # Check if username already exists
        usernames = auth_sheet.col_values(1)
        if username in usernames:
            print("Username exists.")
            return True
        else:
            print("Username not found. Please register first.")
            return False
    except Exception as e:
            print(f"Error during user check: {e}")
            return False
    

def display_welcome_message():
    welcome_message = """
         ___ . .  _                                                                                             
"T$$$P"   |  |_| |_                                                                                             
 :$$$     |  | | |_                                                                                             
 :$$$                                                      "T$$$$$$$b.                                          
 :$$$     .g$$$$$p.   T$$$$b.    T$$$$$bp.                   BUG    "Tb      T$b      T$P   .g$P^^T$$  ,gP^^T$$ 
  $$$    d^"     "^b   $$  "Tb    $$    "Tb    .s^s. :sssp   $$$     :$; T$$P $^b.     $   dP"     `T :$P    `T
  :$$   dP         Tb  $$   :$;   $$      Tb  d'   `b $      $$$     :$;  $$  $ `Tp    $  d$           Tbp.   
  :$$  :$;         :$; $$   :$;   $$      :$; T.   .P $^^    $$$    .dP   $$  $   ^b.  $ :$;            "T$$p.  
  $$$  :$;         :$; $$...dP    $$      :$;  `^s^' .$.     $$$...dP"    $$  $    `Tp $ :$;     "T$$      "T$b 
  $$$   Tb.       ,dP  $$\"""Tb    $$      dP ""$""$" "$"$^^  $$$""T$b     $$  $      ^b$  T$       T$ ;      $$;
  $$$    Tp._   _,gP   $$   `Tb.  $$    ,dP    $  $...$ $..  $$$   T$b    :$  $       `$   Tb.     :$ T.    ,dP 
  $$$;    "^$$$$$^"   d$$     `T.d$$$$$P^"     $  $\"""$ $"", $$$    T$b  d$$bd$b      d$b   "^TbsssP" 'T$bgd$P  
  $$$b.____.dP                                 $ .$. .$.$ss,d$$$b.   T$b.                                       
.d$$$$$$$$$$P  bug                                                    `T$b.

        """
    print(welcome_message)


def start_game():
    print("Starting your journey...")
    questions = quiz_sheet.get_all_records()
    score = 0

    for question in questions:
        print(question['Question'])
        print("Options:")
        for i in range(1, 5):
            print(f"{i}. {question[f'Option {i}']}")

        answer = int(input("Enter your answer (1-4): "))
        if answer == int(question['Answer']):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"Quiz completed. Your score is {score} out of {len(questions)}.")

def main():
    print("Welcome to Lord of the Rings Quiz!")
    display_welcome_message()
    
    while True:  # Loop indefinitely until a successful login or registration
        print("Are you an existing user? (yes/no)")
        existing_user = input().lower()
        
        if existing_user == "no":
            print("Please register to continue.")
            print("Enter a username:")
            username = input("> ")  # Displaying the username prompt differently
            print("Enter a password:")
            password = input("> ")  # Displaying the password prompt differently
            if register(username, password):
                print("Registration successful. Starting the game...")
                start_game()
                break  # Exit the loop if registration is successful
        elif existing_user == "yes":
            print("Enter your username:")
            username = input("> ")  # Displaying the username prompt differently
            print("Enter your password:")
            password = input("> ")  # Displaying the password prompt differently
            if login(username, password):
                print("Login successful. Starting the game...")
                start_game()
                break  # Exit the loop if login is successful
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

main()