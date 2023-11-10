from string import ascii_lowercase, ascii_uppercase


def brute_rot():
    with open("in.txt", "r") as f:
        strings = f.readlines()

    if len(strings) == 0:
        print("Enter at least one string to the in.txt file!")

    base_low = ascii_lowercase * 2
    base_up = ascii_uppercase * 2
    if len(strings) != 0:
        print("=" * 10)
        for string in strings:
            if string.endswith("\n"):
                string = string[:-1]
            print(f"ROT0: {string}")
            for i in range(1, 26):
                new_string = ""
                for letter in string:
                    if letter.lower() == letter and letter in base_low:
                        new_string += base_low[base_low.find(letter) + i]
                    elif letter.lower() != letter and letter in base_up:
                        new_string += base_up[base_up.find(letter) + i]
                    else:
                        new_string += letter
                print(f"ROT{i}: {new_string}")
            print("=" * 10)
        print("NOTE: special symbols might not be translated correctly")


if __name__ == "__main__":
    brute_rot()
