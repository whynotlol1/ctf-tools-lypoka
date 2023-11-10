from encrypted_strings_checker import __data__
from word2number import w2n
import requests


def convert_number():
    with open("in.txt", "r") as f:
        strings = f.readlines()
    with open("key.txt", "r") as f:
        convert_from = f.read()
        if convert_from == "":
            convert_from = "dec"

    if len(strings) == 0:
        print("Enter at least one number to the in.txt file!")
    else:
        for string in strings:
            if string.endswith("\n"):
                string = string[:-1]
            match convert_from:
                case "dec":
                    number = int(string)
                    print(f"Number: {number} [dec]")
                    print(f"Hex: {hex(number).replace("0x", "")}")
                    print(f"Oct: {oct(number).replace("0o", "")}")
                    print(f"Bin: {bin(number).replace("0b", "")}")
                    data = __data__.data
                    data["value"] = number
                    req = requests.post(url="https://dencode.com/dencode", json=data)
                    print(f"Text [dec->text]: {req.json()["response"]["encNumEnShortScale"].lower()}")
                    print("-" * 10)
                case "bin":
                    number = int(string, 2)
                    print(f"Number: {string} [bin]")
                    print(f"Hex: {hex(number).replace("0x", "")}")
                    print(f"Dec: {number}")
                    print(f"Oct: {oct(number).replace("0o", "")}")
                    data = __data__.data
                    data["value"] = number
                    req = requests.post(url="https://dencode.com/dencode", json=data)
                    print(f"Text [dec->text]: {req.json()["response"]["encNumEnShortScale"].lower()}")
                    print("-" * 10)
                case "oct":
                    number = int(string, 8)
                    print(f"Number: {string} [oct]")
                    print(f"Hex: {hex(number).replace("0x", "")}")
                    print(f"Dec: {number}")
                    print(f"Bin: {bin(number).replace("0b", "")}")
                    data = __data__.data
                    data["value"] = number
                    req = requests.post(url="https://dencode.com/dencode", json=data)
                    print(f"Text [dec->text]: {req.json()["response"]["encNumEnShortScale"].lower()}")
                    print("-" * 10)
                case "hex":
                    number = int(string, 16)
                    print(f"Number: {string} [hex]")
                    print(f"Dec: {number}")
                    print(f"Oct: {oct(number).replace("0o", "")}")
                    print(f"Bin: {bin(number).replace("0b", "")}")
                    data = __data__.data
                    data["value"] = number
                    req = requests.post(url="https://dencode.com/dencode", json=data)
                    print(f"Text [dec->text]: {req.json()["response"]["encNumEnShortScale"].lower()}")
                    print("-" * 10)
                case "text":
                    number = w2n.word_to_num(string)
                    print(f"String: {string}")
                    print(f"Hex: {hex(number).replace("0x", "")}")
                    print(f"Dec: {number}")
                    print(f"Oct: {oct(number).replace("0o", "")}")
                    print(f"Bin: {bin(number).replace("0b", "")}")


if __name__ == "__main__":
    convert_number()
