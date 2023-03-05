import requests
import threading
import time
import os

# This will clear the console
os.system('cls' if os.name == 'nt' else 'clear')

print("""\033[91m 

          _____                   _______                  _______                   _____                    _____                    _____          
         /\    \                 /::\    \                /::\    \                 /\    \                  /\    \                  /\    \         
        /::\____\               /::::\    \              /::::\    \               /::\____\                /::\    \                /::\    \        
       /:::/    /              /::::::\    \            /::::::\    \             /:::/    /               /::::\    \              /::::\    \       
      /:::/    /              /::::::::\    \          /::::::::\    \           /:::/    /               /::::::\    \            /::::::\    \      
     /:::/    /              /:::/~~\:::\    \        /:::/~~\:::\    \         /:::/    /               /:::/\:::\    \          /:::/\:::\    \     
    /:::/____/              /:::/    \:::\    \      /:::/    \:::\    \       /:::/____/               /:::/__\:::\    \        /:::/  \:::\    \    
   /::::\    \             /:::/    / \:::\    \    /:::/    / \:::\    \     /::::\    \              /::::\   \:::\    \      /:::/    \:::\    \   
  /::::::\    \   _____   /:::/____/   \:::\____\  /:::/____/   \:::\____\   /::::::\____\________    /::::::\   \:::\    \    /:::/    / \:::\    \  
 /:::/\:::\    \ /\    \ |:::|    |     |:::|    ||:::|    |     |:::|    | /:::/\:::::::::::\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\ ___\ 
/:::/  \:::\    /::\____\|:::|____|     |:::|    ||:::|____|     |:::|    |/:::/  |:::::::::::\____\/:::/__\:::\   \:::\____\/:::/____/     \:::|    |
\::/    \:::\  /:::/    / \:::\    \   /:::/    /  \:::\    \   /:::/    / \::/   |::|~~~|~~~~~     \:::\   \:::\   \::/    /\:::\    \     /:::|____|
 \/____/ \:::\/:::/    /   \:::\    \ /:::/    /    \:::\    \ /:::/    /   \/____|::|   |           \:::\   \:::\   \/____/  \:::\    \   /:::/    / 
          \::::::/    /     \:::\    /:::/    /      \:::\    /:::/    /          |::|   |            \:::\   \:::\    \       \:::\    \ /:::/    /  
           \::::/    /       \:::\__/:::/    /        \:::\__/:::/    /           |::|   |             \:::\   \:::\____\       \:::\    /:::/    /   
           /:::/    /         \::::::::/    /          \::::::::/    /            |::|   |              \:::\   \::/    /        \:::\  /:::/    /    
          /:::/    /           \::::::/    /            \::::::/    /             |::|   |               \:::\   \/____/          \:::\/:::/    /     
         /:::/    /             \::::/    /              \::::/    /              |::|   |                \:::\    \               \::::::/    /      
        /:::/    /               \::/____/                \::/____/               \::|   |                 \:::\____\               \::::/    /       
        \::/    /                 ~~                       ~~                      \:|   |                  \::/    /                \::/____/        
         \/____/                                                                    \|___|                   \/____/                  ~~              
                                                                                                                                                      

\033[0m""")


# Define the functions for sending messages and deleting the webhook
def send_message(webhook_url, message):
    requests.post(webhook_url, json={'content': message})

def delete_webhook(webhook_url):
    requests.delete(webhook_url)

# Define the functions for multithreading
def send_message_threaded(webhook_url, message):
    threading.Thread(target=send_message, args=(webhook_url, message)).start()

def delete_webhook_threaded(webhook_url):
    threading.Thread(target=delete_webhook, args=(webhook_url,)).start()

# Define the main program loop
while True:
    # Ask the user for the webhook URL they want to use
    webhook_url = input('Enter the webhook URL: ')

    # Ask the user what they want to do
    action = input('What would you like to do? (send, delete, exit): ')

    # Handle sending a message
    if action == 'send':
        # Ask the user for the message they want to send
        message = input('Enter the message you want to send: ')

        # Ask the user how many messages they want to send
        num_messages_str = input('How many messages do you want to send? ')
        try:
            num_messages = int(num_messages_str)
        except ValueError:
            print("Invalid number of messages. Please try again.")
            continue

        # Ask the user if they want to send the messages quickly or slowly
        speed = input('Do you want to send the messages quickly or slowly? (fast, slow): ')

        if speed == 'fast':
            # Ask the user how many messages to send before waiting
            num_messages_before_wait_str = input('How many messages should be sent before waiting? ')
            try:
                num_messages_before_wait = int(num_messages_before_wait_str)
            except ValueError:
                print("Invalid number of messages. Please try again.")
                continue

            # Ask the user for the delay time between messages
            delay_time_str = input('Enter the delay time between messages (in seconds): ')
            try:
                delay_time = int(delay_time_str)
            except ValueError:
                print("Invalid delay time. Please try again.")
                continue

            for i in range(num_messages):
                send_message_threaded(webhook_url, message)
                if i % num_messages_before_wait == num_messages_before_wait - 1:
                    time.sleep(delay_time)
        elif speed == 'slow':
            # Ask the user for the delay time between messages
            delay_time_str = input('Enter the delay time between messages (in seconds): ')
            try:
                delay_time = int(delay_time_str)
            except ValueError:
                print("Invalid delay time. Please try again.")
                continue
            for i in range(num_messages):
                send_message(webhook_url, message)
                time.sleep(delay_time)

    # Handle deleting the webhook
    elif action == 'delete':
        # Ask the user if they really want to delete the webhook
        confirm = input('Are you sure you want to delete the webhook? (yes, no): ')

        # Delete the webhook if the user confirms
        if confirm == 'yes':
            # Ask the user if they want to delete the webhook quickly or slowly
            speed = input('Do you want to delete the webhook quickly or slowly? (fast, slow): ')

            # Delete the webhook either quickly with multithreading or slowly with a delay
            if speed == 'fast':
                delete_webhook_threaded(webhook_url)

os.system('cls' if os.name == 'nt' else 'clear')
