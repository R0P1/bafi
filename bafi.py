:: Program : BAFI
:: Description : Collect information about WI-FI profiles stored on the computer.
:: Author : R0P1
:: Github: https://github.com/R0P1/bafi.git

import os

while True:
    perintah = "netsh wlan show profile"
    os.system(perintah)
    user_profile = input("Select a user profie (or type 'E' to exit): ")
    if user_profile == "E":
        exit(0)
    else:
        os.system(f"{perintah} {user_profile} key=clear")
        continue
