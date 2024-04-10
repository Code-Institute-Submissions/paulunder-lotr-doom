import json
import os
import gspread
from google.oauth2.service_account import Credentials
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


def register(username, password):
    """
    Function to register a new user, checks in the Google
    sheet if the username already exists.
    """
    try:
        usernames = auth_sheet.col_values(1)
        if username == "" or password == "":
            print("Username or password cannot be empty.")
            return False
        else:
            if username in usernames:
                print("Please choose a different username.")
                return False
            auth_sheet.append_row([username, password])
            print("\nRegistration successful. You can now log in.")
            return True
    except Exception as e:
        print(f"Error during registration: {e}")
        return False


def login(username, password):
    """
    Function to login an existing user, checks in the Google sheet
    if the username exists and if the password is correct.
    """
    try:
        usernames = auth_sheet.col_values(1)
        if username not in usernames:
            print("\nUsername not found. Please register first.")
            return False
        index = usernames.index(username) + 1
        stored_password = auth_sheet.cell(index, 2).value
        if password == stored_password:
            print("\nLogin successful.")
            return True
        else:
            print("\nIncorrect password.")
            return False
    except Exception as e:
        print(f"Error during login: {e}")
        return False


def check_user(username):
    """
    Function to check if the user already exists in the Google sheet.
    """
    try:
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
| |  / \\|_)| \\ |     `'   ,','  _,-'___________`-._  `.`.
| |__\\_/| \\|_/ |        ,','  ,'_,-'     .     `-._`.  `.`.
|              |       /,'  ,','        >|<        `.`.  `.\\
| OF THE  _ _  |      //  ,','      ><  ,^.  ><      `.`.  \\\\
| |_)||\\|/_(_  |     //  /,'      ><   / | \\   ><      `.\\  \\\\
| | \\|| |\\_|_) |    //  //      ><    \\/\\^/\\/    ><      \\\\  \\\\
|______________|   ;;  ;;              `---'              ::  ::
                   ||  ||              (____              ||  ||
 DOORS OF DURIN   _||__||_            ,'----.            _||__||_
                 (o.____.o)____        `---'        ____(o.____.o)
                   |    | /,--.)                   (,--.\\ |    |
                   |    |((  -`___               ___`   ))|    |
                   |    | \\\\,'',  `.           .'  .``.// |    |
                   |    |  // (___,'.         .'.___) \\\\  |    |
                  /|    | ;;))  ____) .     . (____  ((\\\\ |    |\\
                  \\|.__ | ||/ .'.--.\\/       `/,--.`. \\;: | __,|;
                   |`-,`;.| :/ /,'  `)-'   `-('  `.\\ \\: |.;',-'|
                   |   `..  ' / \\__.'         `.__/ \\ `  ,.'   |
                   |    |,\\  /,                     ,\\  /,|    |
                   |    ||: : )          .          ( : :||    |
                  /|    |:; |/  .      ./|\\,      ,  \\| :;|    |\\
                  \\|.__ |/  :  ,/-    <--:-->    ,\\.  ;  \\| __,|;
                   |`-.``:   `'/-.     '\\|/`     ,-\\`;   ;'',-'|
                   |   `..   ,' `'       '       `  `.   ,.'   |
                   |    ||  :                         :  ||    |
                   |    ||  |                         |  ||    |
                   |    ||  |                         |  ||    |
                   |    |'  |            _            |  `|    |
                   |    |   |          '|))           |   |    |
                   ;____:   `._        `'           _,'   ;____:
                  {______}     \\___________________/     {______}
              SSt |______|_______________________________|______|
        """
    print(welcome_message)


def display_mordor():
    mordor_message = """
                       /\\
        _/\\           /  \\
    _  /   \\         /    \\/\\
   / \\/   _ \\     /\\/\\  _  _/\\
  /   \\_ / \\/\\_/\\/_/  \\/ \\/   \\
 /\\/\\   \\_   /   \\/            \\
/    \\___/\\ /     \\             \\
           \\       \\             \\
           .-"---.  \\             \\
__..---.. /       \\  \\             \\
         /\\___.-'./\\''--..____..--''
`-.      \\/ O) (O \\/ ''--.._
    __    |  (_)  |         _.-'-._
   / /  __/\\\\___//\\__ ..--''-._
   | (_/\\ \\/`---'\\/ /\\         `-._
_.-\\ \\/  \\  \\   /  /  \\.-'-._
   /\\|   /  -| |-  \\   \\     `-._

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
:. . .| |  ((<))  | |,          ,       ,             |\\'__',-._.' ' ||. .:
.:.:. | |   `-'   | |---....____                      | ,---\\/--/  ' ||:.:.
------| |         : :    ,.     ```--..._   ,         |''  '  '  ' ' ||----
_...--. |  ,       \\ \\             ,.    `-._     ,  /: '  '  '  ' ' ;;..._
:.:. .| | -O-       \\ \\    ,.                `._    / /:'  '  '  ' ':: .:.:
.:. . | |_(`__       \\ \\                        `. / / :'  '  '  ' ';;. .:.
:. . .<' (_)  `>      `.`.          ,.    ,.     ,','   \\  '  '  ' ;;. . .:
.:. . |):-.--'(         `.`-._  ,.           _,-','      \\ '  '  '//| . .:.
:. . .;)()(__)(___________`-._`-.._______..-'_.-'_________\\'  '  //_:. . .:
.:.:,' \\/\\/--\\/--------------------------------------------`._',;'`. `.:.:.
:.,' ,' ,'  ,'  /   /   /   ,-------------------.   \\   \\   \\  `. `.`. `..:
,' ,'  '   /   /   /   /   //                   \\\\   \\   \\   \\   \\  ` `.
,'  '    /   /   /   /   /((  Lord of the Rings  ))\\   \\   \\   \\   \\   `
        """
    print(winning_message)


def start_game():
    """
    Function to start the game - load the story from the JSON file and
    display the questions, handles user input and displays the result.
    """
    while True:
        print("\nStarting your journey...")
        with open('story.json', 'r') as file:
            story = json.load(file)
        paths = story['paths']
        print("\nChoose a path to start your journey:")
        print("--------------------")
        print("1. Path of the Ring")
        print("OR")
        print("2. Path of the Fellowship")
        selected_path = input("Choose a path (1/2): ")
        if selected_path == '1' or selected_path == '2':
            if selected_path == '1':
                selected_path = paths[0]
                print(selected_path['start'])
                questions = story['questions'][0:8]
            else:
                selected_path = paths[1]
                print(selected_path['start'])
                questions = story['questions'][8:16]
        else:
            print("Invalid input. Please enter '1' or '2'.")
            print("\n Restarting the game...")
            start_game()
            break
        score = 0
        for question in questions:
            print(Fore.GREEN + question['question'] + Fore.RESET)
            print("--------------------")
            for option in question['options']:
                print(option)
            print("--------------------")
            answer = input("> ").lower()
            if answer == 'a' or answer == 'b':
                if answer == question['correct_answer']:
                    print("Well done! Your choice has led to success.")
                    print("--------------------")
                    print("You get closer to Mordor!")
                    print("--------------------")
                    display_mordor()
                    score += 1
                else:
                    print("\nOops! Your choice has led to a setback.")
                    print("You took the wrong path. Restart? (yes/no)")
                    restart_choice = input("> ").lower()
                    if restart_choice == 'yes' or restart_choice == 'no':
                        if restart_choice == 'yes':
                            break
                        else:
                            print("Thank you for playing!")
                            return
                    else:
                        print("Invalid input.")
                        print("\n\n restarting game...")
                        break
                if score == len(selected_path['questions']):
                    print("\nYou have successfully completed the journey.")
                    if score > 6:
                        print("\nYou have saved Middle Earth!\n")
                        display_winning_message()
                    else:
                        print("\n\n\n\nMiddle Earth is burning. You lose.")
                    print("\nWould you like to play again? (yes/no)\n")
                    play_again = input("> ").lower()
                    if play_again == 'yes' or play_again == 'no':
                        if play_again != 'yes':
                            print("\nThank you for playing!")
                            break
                        else:
                            print("\nThank you for playing!")
                            print("\ntake you back to menu...")
                            signing()
                        break
                    else:
                        print("Invalid input.")
                        print("\n\n take you back to menu...")
                        signing()
                        break
            else:
                print("Invalid input. Please enter 'a' or 'b'.")
                break


def signing():
    """
    Function to handle user registration and login.
    """
    print("\n\nAre you an existing user? (yes/no)")
    existing_user = input("> ").lower()
    if existing_user == "no":
        print("\nPlease register to continue.")
        print("\nEnter a username:")
        username = input("> ")
        print("\nEnter a password:")
        password = input("> ")
        if register(username, password):
            print("\nRegistration successful. \n\nStarting the game...")
            start_game()
        else:
            print("\nRegistration failed. Please try again.")
            signing()
    elif existing_user == "yes":
        print("\nEnter your username:")
        username = input("> ")
        print("\nEnter your password:")
        password = input("> ")
        if login(username, password):
            print("\n\nLogin successful. \nStarting the game...")
            start_game()
        else:
            print("\nLogin failed. Please try again.")
            signing()
    else:
        print("\nInvalid input. Please enter 'yes' or 'no'.")
        signing()


def main():
    print("Welcome to Lord of the Rings Quiz!")
    display_welcome_message()
    signing()


main()
