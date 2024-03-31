# Write your code to expect a terminal of 80 characters wide and 24 rows high


import random
import gspread
from google.oauth2.service_account import Credentials
import json
import os
from colorama import Fore


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


creds_json = os.environ.get('CREDS')

CREDS = Credentials.from_service_account_info(json.loads(creds_json))

SCOPED_CREDS = CREDS.with_scopes(SCOPE)

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open('LordOfTheRings')



auth_sheet = SHEET.worksheet('Auth')


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
 ______________     _             _,-----------._        ___
|              |   (_,.-      _,-'_,-----------._`-._    _)_)
| THE _  _  _  |      |     ,'_,-'  ___________  `-._`.
| |  / \|_)| \ |     `'   ,','  _,-'___________`-._  `.`.
| |__\_/| \|_/ |        ,','  ,'_,-'     .     `-._`.  `.`.
|              |       /,'  ,','        >|<        `.`.  `.\
| OF THE  _ _  |      //  ,','      ><  ,^.  ><      `.`.  \\
| |_)||\|/_(_  |     //  /,'      ><   / | \   ><      `.\  \\
| | \|| |\_|_) |    //  //      ><    \/\^/\/    ><      \\  \\
|______________|   ;;  ;;              `---'              ::  ::
                   ||  ||              (____              ||  ||
 DOORS OF DURIN   _||__||_            ,'----.            _||__||_
                 (o.____.o)____        `---'        ____(o.____.o)
                   |    | /,--.)                   (,--.\ |    |
                   |    |((  -`___               ___`   ))|    |
                   |    | \\,'',  `.           .'  .``.// |    |
                   |    |  // (___,'.         .'.___) \\  |    |
                  /|    | ;;))  ____) .     . (____  ((\\ |    |\
                  \|.__ | ||/ .'.--.\/       `/,--.`. \;: | __,|;
                   |`-,`;.| :/ /,'  `)-'   `-('  `.\ \: |.;',-'|
                   |   `..  ' / \__.'         `.__/ \ `  ,.'   |
                   |    |,\  /,                     ,\  /,|    |
                   |    ||: : )          .          ( : :||    |
                  /|    |:; |/  .      ./|\,      ,  \| :;|    |\
                  \|.__ |/  :  ,/-    <--:-->    ,\.  ;  \| __,|;
                   |`-.``:   `'/-.     '\|/`     ,-\`;   ;'',-'|
                   |   `..   ,' `'       '       `  `.   ,.'   |
                   |    ||  :                         :  ||    |
                   |    ||  |                         |  ||    |
                   |    ||  |                         |  ||    |
                   |    |'  |            _            |  `|    |
                   |    |   |          '|))           |   |    |
                   ;____:   `._        `'           _,'   ;____:
                  {______}     \___________________/     {______}
              SSt |______|_______________________________|______|
        """
    print(welcome_message)

def display_mordor():
    mordor_message = """
                        
                       /\\
        _/\\           /  \\
    _  /   \\         /    \/\\
   / \/   _ \\     /\/\\  _  _/\\
  /   \_ / \/\_/\/_/  \/ \/   \\
 /\/\\   \_   /   \/            \\
/    \___/\\ /     \\             \\
           \\       \\             \\
           .-"---.  \\             \\
__..---.. /       \\  \\             \\
         /\___.-'./\''--..____..--''
`-.      \/ O) (O \/ ''--.._
    __    |  (_)  |         _.-'-._
   / /  __/\\\___//\__ ..--''-._
   | (_/\\ \/`---'\/ /\\         `-._
_.-\\ \/  \\  \\   /  /  \.-'-._
   /\|   /  -| |-  \\   \\     `-._

        """
    print(mordor_message)

def display_winning_message():
    winning_message = """
                    . .:.:.:.:. .:\\     /:. .:.:.:.:. ,
               .-._  `..:.:. . .:.:`- -':.:. . .:.:.,'  _.-.
              .:.:.`-._`-._..-''_...---..._``-.._.-'_.-'.:.:.
           .:.:. . .:_.`' _..-''._________,``-.._ `.._:. . .:.:.
        .:.:. . . ,-'_.-''      ||_-(O)-_||      ``-._`-. . . .:.:.
       .:. . . .,'_.'           '---------'           `._`.. . . .:.
     :.:. . . ,','               _________               `.`. . . .:.:
    `.:.:. .,','            _.-''_________``-._            `._.     _.'
  -._  `._./ /            ,'_.-'' ,       ``-._`.          ,' '`:..'  _.-
 .:.:`-.._' /           ,','                   `.`.       /'  '  \\.-':.:.
 :.:. . ./ /          ,','               ,       `.`.    / '  '  '\\. .:.:
:.:. . ./ /          / /    ,                      \\ \\  :  '  '  ' \\. .:.:
.:. . ./ /          / /            ,          ,     \\ \\ :  '  '  ' '::. .:.
:. . .: :    o     / /                               \\ ;'  '  '  ' ':: . .:
.:. . | |   /_\\   : :     ,                      ,    : '  '  '  ' ' :: .:.
:. . .| |  ((<))  | |,          ,       ,             |\'__',-._.' ' ||. .:
.:.:. | |   `-'   | |---....____                      | ,---\/--/  ' ||:.:.
------| |         : :    ,.     ```--..._   ,         |''  '  '  ' ' ||----
_...--. |  ,       \\ \\             ,.    `-._     ,  /: '  '  '  ' ' ;;..._
:.:. .| | -O-       \\ \\    ,.                `._    / /:'  '  '  ' ':: .:.:
.:. . | |_(`__       \\ \\                        `. / / :'  '  '  ' ';;. .:.
:. . .<' (_)  `>      `.`.          ,.    ,.     ,','   \\  '  '  ' ;;. . .:
.:. . |):-.--'(         `.`-._  ,.           _,-','      \\ '  '  '//| . .:.
:. . .;)()(__)(___________`-._`-.._______..-'_.-'_________\'  '  //_:. . .:
.:.:,' \/\/--\/--------------------------------------------`._',;'`. `.:.:.
:.,' ,' ,'  ,'  /   /   /   ,-------------------.   \\   \\   \\  `. `.`. `..:
,' ,'  '   /   /   /   /   //                   \\\   \\   \\   \\   \\  ` `.SSt
,'  '    /   /   /   /   /((  Lord of the Rings  ))\\   \\   \\   \\   \\   `  `

        """ 
    print(winning_message)


def start_game():
    while True:
        print("Starting your journey...")
        # Load the story from the JSON file
        with open('story.json', 'r') as file:
            story = json.load(file)
        
        paths = story['paths']
        
        # Select a random path
        selected_path = random.choice(paths)
        
        print(selected_path['start'])
        
        questions = story['questions']
        score = 0  # Initialize the score
        
        # Display questions based on the selected path
        for question_id in selected_path['questions']:
            question = [q for q in questions if q['id'] == question_id][0]
            print(question['question'])
            print("--------------------")
            for option in question['options']:
                print(option)
            print("--------------------")
            answer = input("> ").lower()
            if answer == question['correct_answer']:
                print("Well done! Your choice has led to success.")
                print("--------------------")
                print("You get closer to Mordor!")
                print("--------------------")
                display_mordor()
                score += 1  # Increment the score for correct answers
            else:
                print("Oops! Your choice has led to a setback.")
                print("You took the wrong path. Would you like to restart the game? (yes/no)")
                restart_choice = input("> ").lower()
                if restart_choice == 'yes':
                    break  # Break out of the loop and restart the game
                else:
                    print("Thank you for playing!")
                    return  # End the game if the player chooses not to restart
        
        if score == len(selected_path['questions']):
            print("Congratulations! You have successfully completed the journey.")
            if score > 6:
                print("\nYou have saved Middle Earth!\n")
                display_winning_message()
            else:
                print("Middle Earth is burning. You lose.")
            
            print("\nWould you like to play again? (yes/no)\n")
            play_again = input("> ").lower()
            if play_again != 'yes':
                print("Thank you for playing!")
                break

            print(f"Your final score is: {score}/{len(selected_path['questions'])}")
            break  



def main():
    print("Welcome to Lord of the Rings Quiz!")
    display_welcome_message()
    print("Are you an existing user? (yes/no)")
    try:
        existing_user = input("> ")
    except ValueError:
        print("Invalid input. Please enter 'yes' or 'no'.")
        return

    if existing_user == "no":
        print("Please register to continue.")
        print("Enter a username:")
        username = input("> ")
        print("Enter a password:")
        password = input("> ")
        if register(username, password):
            print("Registration successful. Starting the game...")
            start_game()
    elif existing_user == "yes":
        print("Enter your username:")
        username = input("> ")
        print("Enter your password:")
        password = input("> ")
        if login(username, password):
            print("Login successful. Starting the game...")
            start_game()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

main()