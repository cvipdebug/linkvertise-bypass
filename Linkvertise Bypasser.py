import requests, gratient
from os import system

system("cls && title CVIP LINKVERTISE BYPASSER")
def main():
    try:
        Banner = (gratient.purple("""
            ▓██▓     ██▓ ███▄    █  ██ ▄█▀    ▄▄▄▄   ▓██   ██▓ ██▓███   ▄▄▄        ██████   ██████ ▓█████  ██▀███  
            ▓██▒    ▓██▒ ██ ▀█   █  ██▄█▒    ▓█████▄  ▒██  ██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒
            ▒██░    ▒██▒▓██  ▀█ ██▒▓███▄░    ▒██▒ ▄██  ▒██ ██░▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒███   ▓██ ░▄█ ▒
            ▒██░    ░██░▓██▒  ▐▌██▒▓██ █▄    ▒██░█▀    ░ ▐██▓░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  
            ░██████▒░██░▒██░   ▓██░▒██▒ █▄   ░▓█  ▀█▓  ░ ██▒▓░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░▒████▒░██▓ ▒██▒
            ░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒   ░▒▓███▀▒   ██▒▒▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░
            ░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░   ▒░▒   ░  ▓██ ░▒░ ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░
            ░ ░    ▒ ░   ░   ░ ░ ░ ░░ ░     ░    ░  ▒ ▒ ░░  ░░         ░   ▒   ░  ░  ░  ░  ░  ░     ░     ░░   ░ 
                ░  ░ ░           ░ ░  ░       ░       ░ ░                    ░  ░      ░        ░     ░  ░   ░     
                                                ░  ░ ░                                                          

                                                                                                                                    
                                    c       v       i       p
        """))

        def purple(text):
            system(""); faded = ""
            red = 35
            for character in text:
                red += 3
                if red > 255:
                    red = 255
                faded += (f"\033[38;2;{red};0;220m{character}")
            return faded

        File = open("Link.txt", "a")
        print(Banner)
        url = input(purple(" [>] Linkvertise link : "))

        API = f"https://bypass.bot.nu/bypass2?url={url}"#Other API https://bypass.bot.nu/bypass2?url= Or https://soud.me/api/Bypass?url= or https://bypass.bot.nu/bypass2?url=

        data = requests.get(f"https://bypass.bot.nu/bypass2?url={url}")
        link = data.json()["destination"]

        system("cls")
        print(Banner)
        print(gratient.green(f" [>] Destination link : {link}"))

        File.write(f"{link}" + "\n")

        system("pause >nul")
        File.close()
    except:
        system("cls")
        print(Banner)
        print(purple(" [>] Bro use a working URL hit eniter to go back"))
        system("pause >nul")
        system("cls")
        main()
main()
