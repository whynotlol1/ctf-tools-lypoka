from encrypted_strings_checker import __data__
import requests


def check_encrypted_string():
    with open("in.txt", "r") as f:
        strings = f.readlines()

    with open("key.txt", "r") as f:
        keyword = f.read()

    if len(strings) == 0:
        print("Enter at least one string to the in.txt file!")
    if keyword == "":
        print("Enter the keyword to the key.txt file!")

    if len(strings) != 0 and keyword != "":
        count_success = 0
        for string in strings:
            if string.endswith("\n"):
                string = string[:-1]
            data = __data__.data
            data["value"] = f"{string}"
            req = requests.post(url="https://dencode.com/dencode", json=data)
            if keyword in req.text:
                print(f"Keyword found: {req.text[req.text.find(keyword):req.text.find('"', req.text.find(keyword))]}")
                count_success += 1
        if count_success == 0:
            print(f"{keyword} wasn't found in any of the input strings!")


if __name__ == "__main__":
    check_encrypted_string()
