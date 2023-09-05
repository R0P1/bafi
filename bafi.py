import os

while True:
    os.system("cls")
    perintah = "netsh wlan show profile"
    os.system(perintah)
    user_profile = input("Select a user profie (or type 'E' to exit): ")
    if user_profile == "E":
        exit(0)
    else:
        os.system(f"{perintah} {user_profile} key=clear")
        continue
