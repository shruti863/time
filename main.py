import os
import time
import requests
import pytz
import logging
from datetime import datetime
import socket
from time import sleep
from bs4 import BeautifulSoup
import uuid
from PIL import Image
import io

API_VERSION = 'v15.0'

HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

os.system('clear')

# Colored text definitions
brown_text = "\033[0;33m"
yellow_text = "\033[1;33m"
red_text = "\033[1;31m"
green_text = "\033[1;32m"
cyan_text = "\033[1;36m"
blue_text = "\033[1;34m"
magenta_text = "\033[1;35m"
pink_text = "\033[1;38;5;206m"  # Pink
purple_text = "\033[1;38;5;90m"  # Purple
golden_text = "\033[1;38;5;178m"  # Golden
teal_text = "\033[1;38;5;30m"  # Teal
orange_text = "\033[1;38;5;208m"  # Orange
midnight_blue_text = "\033[1;38;5;17m"  # Midnight Blue
khaki_text = "\033[1;38;5;185m"  # Khaki
coral_text = "\033[1;38;5;209m"  # Coral
reset_text = "\033[0m"

additional_logo = f"""\033[1;32m

  _______ _____  ____  _____            _   _ _____  
 |__   __/ ____||  _ \|  __ \     /\   | \ | |  __ \ 
    | | | (___  | |_) | |__) |   /  \  |  \| | |  | |
    | |  \___ \ |  _ <|  _  /   / /\ \ | . ` | |  | |
    | |_ ____) || |_) | | \ \  / ____ \| |\  | |__| |
    |_(_)_____(_)____/|_|  \_\/_/    \_\_| \_|_____/ 
{reset_text}
"""
logo = f"""
{teal_text}
     \033[1;36m╔═════════════════════════════════════╗
     \033[1;36m║                                     ║
     \033[1;36m║       \033[1;35mCREDIT => T.S. BRAND          \033[1;36m║
     \033[1;36m║       \033[1;35mOWNER => SATISH               \033[1;36m║
     \033[1;36m║       \033[1;35mWATSAPP => +916268781574      \033[1;36m║
     \033[1;36m║                                     ║
     \033[1;36m╚═════════════════════════════════════╝
{reset_text}
"""
made_by_text = f"{orange_text}          FEEL THE POWER OF T.S.BRAND {reset_text}\n\n"

def display_background_image():
    try:
        # Load the image
        image_url = "https://raw.githubusercontent.com/shruti863/time/master/TS.jpg"
        response = requests.get(image_url)
        image = Image.open(io.BytesIO(response.content))

        # Resize the image to fit the terminal window
        terminal_size = (os.get_terminal_size().columns, os.get_terminal_size().lines)
        resized_image = image.resize(terminal_size)

        # Display the image
        resized_image.show()
    except Exception as e:
        print_red(f"Error displaying background image: {e}")

def is_internet_available():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True
    except OSError:
        pass
    return False

def get_user_name(access_token):
    try:
        response = requests.get(f'https://graph.facebook.com/{API_VERSION}/me', params={'access_token': access_token})
        response.raise_for_status()
        user_data = response.json()
        return user_data.get('name', 'Unknown User')
    except requests.exceptions.RequestException as e:
        logging.error(f"{red_text}Error fetching user name: {e}{reset_text}")
        return 'Unknown User'

def send_message(api_url, access_token, thread_id, message):
    parameters = {'access_token': access_token, 'message': message}
    try:
        response = requests.post(api_url, data=parameters, headers=HEADERS)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"{red_text}Error sending message: {e}{reset_text}")
        return None

def get_colored_input(prompt, color_code):
    user_input = input(f"{color_code}{prompt}{reset_text}")
    return user_input


def print_brown(text):
    print(f"{brown_text}{text}{reset_text}")

def print_yellow(text):
    print(f"{yellow_text}{text}{reset_text}")

def print_red(text):
    print(f"{red_text}{text}{reset_text}")

def print_green(text):
    print(f"{green_text}{text}{reset_text}")

def print_cyan(text):
    print(f"{cyan_text}{text}{reset_text}")

def print_blue(text):
    print(f"{blue_text}{text}{reset_text}")

def print_magenta(text):
    print(f"{magenta_text}{text}{reset_text}")

def print_pink(text):
    print(f"{pink_text}{text}{reset_text}")

def print_purple(text):
    print(f"{purple_text}{text}{reset_text}")

def print_golden(text):
    print(f"{golden_text}{text}{reset_text}")

def print_teal(text):
    print(f"{teal_text}{text}{reset_text}")

def print_orange(text):
    print(f"{orange_text}{text}{reset_text}")

def print_midnight_blue(text):
    print(f"{midnight_blue_text}{text}{reset_text}")

def print_khaki(text):
    print(f"{khaki_text}{text}{reset_text}")

def print_coral(text):
    print(f"{coral_text}{text}{reset_text}")

# ... (rest of the script)


def get_access_tokens():
    choice = get_colored_input("   \033[1;38;5;208m❦ ════════════════ •⊰❂⊱• ════════════════ ❦\n\n  \033[1;32m『1』 INPUT TOKEN FILE \n  『2』 INPUT TOKEN \n\n   \033[1;31m✓CHOOSE => ", pink_text)

    if choice == '1':
        try:
            file_path = get_colored_input("\n\033[1;35mEnter Token File Path :- ", magenta_text)
            with open(file_path, 'r') as file:
                access_tokens = file.read().splitlines()
        except FileNotFoundError:
            print_red(f"{red_text}File not found. Please provide a valid file path.{reset_text}")
            exit()
    elif choice == '2':
        num_tokens = int(get_colored_input("   \nEnter Token Number :-  ", purple_text))
        access_tokens = [get_colored_input(f"Enter access token {i + 1}: ", golden_text) for i in range(num_tokens)]
    else:
        print_red(f"{red_text}Invalid choice. Exiting.{reset_text}")
        exit()

    return access_tokens

def get_thread_ids():
    choice = get_colored_input("   \033[1;38;5;208m❦ ════════════════ •⊰❂⊱• ════════════════ ❦\n\n  \033[1;32m『1』 INPUT GROUP/INBOX ID FILE \n  \033[1;32m『2』 INPUT GROUP/INBOX ID \n\n   \033[1;31m✓CHOOSE => ", khaki_text)

    if choice == '1':
        try:
            file_path = get_colored_input("   \n\033[1;35mEnter Group/Inbox File Path :- ", coral_text)
            with open(file_path, 'r') as file:
                thread_ids = file.read().splitlines()
        except FileNotFoundError:
            print_red(f"{red_text}File not found. Please provide a valid file path.{reset_text}")
            exit()
    elif choice == '2':
        num_threads = int(get_colored_input("   \nEnter Group/Inbox Number :- ", khaki_text))
        thread_ids = [get_colored_input(f"Enter thread ID {i + 1}: ", coral_text) for i in range(num_threads)]
    else:
        print_red(f"{red_text}Invalid choice. Exiting.{reset_text}")
        exit()

    return thread_ids

def get_access_tokens_and_thread_ids():
    access_tokens = get_access_tokens()
    thread_ids = get_thread_ids()
    return access_tokens, thread_ids

def round_robin_send_messages(access_tokens, thread_ids, messages, mn, sleep_time):
    ist = pytz.timezone('Asia/Kolkata')

    num_tokens = len(access_tokens)
    num_threads = len(thread_ids)
    num_messages = len(messages)
    current_message_index = 0

    while True:
        for j in range(num_tokens):
            access_token = access_tokens[j]
            user_name = get_user_name(access_token)

            for k in range(num_threads):
                thread_id = thread_ids[k]
                api_url = f'https://graph.facebook.com/{API_VERSION}/t_{thread_id}/'
                current_message = messages[current_message_index]
                message = f'{mn} {current_message}'

                response = send_message(api_url, access_token, thread_id, message)
                current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

                if response and response.status_code == 200:
                    print_green(f"\n          \033[1;31m╭─────────Ⓣ.Ⓢ.ⒷⓇⒶⓃⒹ─────────╮\n          \033[1;31m☒FEEL THE POWER OF T.S.BRAND☒\n          \033[1;31m╰─────────Ⓣ.Ⓢ.ⒷⓇⒶⓃⒹ─────────╯\n\033[1;32m[✓]{user_name} Message Send Successfully. \n\033[1;32m✪Group Id :- {thread_id} \n\033[1;32m✪Hater Name :- {mn} \n\033[1;32m✪Message :- {message} \n\033[1;38;5;208m⏰Time :- {current_time}")
                else:
                    print_red(f"{red_text}Failed To Send Message Satish Sir Please Help {user_name} To Group Id {thread_id}: {message}{reset_text}")

                sleep(sleep_time)

        current_message_index = (current_message_index + 1) % num_messages

def main():
	display_background_image()
        print_blue(additional_logo)
        print_yellow(logo)
        print_yellow(made_by_text)
        logging.basicConfig(level=logging.INFO)

    while True:
        try:
            while not is_internet_available():
                print_red("\n Net Problem \nInternet Connection Not Available. Waiting For Connection...")
                sleep(10)

            access_tokens, thread_ids = get_access_tokens_and_thread_ids()
            mn_color = get_colored_input("\n\033[1;36mEnter Hater Name :- ", purple_text)
            txt_file_path = get_colored_input("\n\033[1;36mEnter Message File Path :- ", golden_text)

            try:
                with open(txt_file_path, 'r') as file:
                    messages = file.read().splitlines()
            except FileNotFoundError:
                print_red("File not found. Please provide a valid file path.")
                exit()

            sleep_time = float(get_colored_input("\n\033[1;36mEnter Speed Time (second) :- ", teal_text))

            round_robin_send_messages(access_tokens, thread_ids, messages, mn_color, sleep_time)

        except KeyboardInterrupt:
            logging.info(f"{brown_text}\nScript terminated by user.{reset_text}")

if __name__ == "__main__":
	main()
