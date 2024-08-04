import requests
import os
import datetime
from colorama import Fore, Style, init
from tkinter import Tk
from tkinter.filedialog import askopenfilename

init(autoreset=True)

def display_header():
    ascii_art = '''

     ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ ▄▄   ▄▄ ▄▄▄▄▄▄▄ 
    █  ▄    █   ▄  █ █       █  █▄█  █       █  █ █  █       █
    █ █▄█   █  █ █ █ █    ▄▄▄█       █   ▄   █  █▄█  █    ▄▄▄█
    █       █   █▄▄█▄█   █▄▄▄█       █  █ █  █       █   █▄▄▄ 
    █  ▄   ██    ▄▄  █    ▄▄▄█       █  █▄█  █       █    ▄▄▄█
    █ █▄█   █   █  █ █   █▄▄▄█ ██▄██ █       ██     ██   █▄▄▄ 
    █▄▄▄▄▄▄▄█▄▄▄█  █▄█▄▄▄▄▄▄▄█▄█   █▄█▄▄▄▄▄▄▄█ █▄▄▄█ █▄▄▄▄▄▄▄█

                '''
    print(Fore.RED + Style.BRIGHT + ascii_art)
    timestamp = datetime.datetime.now().strftime('[#-%d-%m-%Y %H:%M:%S!]->')
    print(Fore.YELLOW + Style.BRIGHT + timestamp)
    print(Fore.GREEN + Style.BRIGHT + "[#-Acces Granted!]->")

def get_image_path():
    Tk().withdraw()
    input(Fore.CYAN + Style.BRIGHT + "[#-Press [-Enter-] To Select Image And Remove Background!]->")
    file_path = askopenfilename()
    if not file_path:
        print(Fore.RED + Style.BRIGHT + "[#-No File Selected! - Exiting Program.....!]->")
        exit()
    return file_path

def remove_background(image_path, api_key):
    print(Fore.YELLOW + Style.BRIGHT + f"[#-Processing Image:{image_path}!]->")

    with open(image_path, 'rb') as file:
        image_data = file.read()

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': image_data},
        data={'size': 'auto'},
        headers={'X-Api-Key': api_key},
    )

    if response.status_code == requests.codes.ok:
        result_dir = "bremove_results"
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)
        
        result_path = os.path.join(result_dir, "output.png")
        with open(result_path, 'wb') as out_file:
            out_file.write(response.content)
        print(Fore.GREEN + Style.BRIGHT + f"[#-Result Succesfully Saved To:{result_path}!]->")
    else:
        print(Fore.RED + Style.BRIGHT + f"[#-Error:{response.status_code}!]->")
        print(response.text)

def main():
    display_header()
    api_key = 'Drop Your API Key Here!'
    if not api_key:
        print(Fore.RED + Style.BRIGHT + "[#-Please! - Provide Your RemoveBG API Key!]->")
        exit()

    image_path = get_image_path()
    remove_background(image_path, api_key)

if __name__ == "__main__":
    main()