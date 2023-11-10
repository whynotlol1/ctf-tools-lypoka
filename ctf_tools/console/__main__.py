from encrypted_strings_checker.check_encrypted_string import check_encrypted_string
from number_converter.convert_number import convert_number
from ROT_bruteforce.brute_rot import brute_rot
from url_scanner.scan_url import scan_url


def main():
    commands = {
        "=check=str": {
            "-s": "string",
            "-k": "key"
        },
        "=convert=num": {
            "-s": "string / number",
            "-k": "key"
        },
        "=brute=rot": {
            "-s": "string"
        },
        "=check=url": {
            "-url": "url",
            "-k": "key"
        },
        "-h": "help",
        "-c": "clear",
        "-q": "quit"
    }
    while True:
        task = input().split(" ")
        if task[0] == "-h":
            for command in commands.keys():
                print(f"{command}: {commands[command]}")
        if task[0] == "-q":
            exit(0)
        if task[0] == "-c":
            for _ in range(1000):
                print()

        if task[0] not in commands:
            print("Unknown command")
        else:
            match task[0]:
                case "=check=str":
                    with open("in.txt", "w") as f:
                        f.write(task[2])
                    with open("key.txt", "w") as f:
                        f.write(task[4])
                    check_encrypted_string()
                case "=convert=num":
                    with open("in.txt", "w") as f:
                        f.write(task[2])
                    with open("key.txt", "w") as f:
                        f.write(task[4])
                    convert_number()
                case "=brute=rot":
                    with open("in.txt", "w") as f:
                        f.write(task[2])
                    brute_rot()
                case "=check=url":
                    with open("in.txt", "w") as f:
                        f.write(task[2])
                    with open("key.txt", "w") as f:
                        f.write(task[4])
                    scan_url()


if __name__ == "__main__":
    main()
