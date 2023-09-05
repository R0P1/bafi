import os

while True:
    os.system("cls")
    command = "netsh wlan show profile"
    os.system(command)
    user_profile = input("Select a user profie (or type 'E' to exit): ")
    if user_profile == "E":
        exit(0)
    else:
        
        os.system(f"{command} {user_profile} key=clear")
        c = input("Press any key to continue...")
        continue
