import subprocess


def sqlm_run():
    with open("in.txt", "r") as f:
        urls = f.readlines()

    with open("params.txt", "r") as f:
        params = f.read()

    if len(urls) == 0:
        print("Enter at least one url to the in.txt file!")
    if params == "":
        print("Enter at least one SQLM parameter to the params.txt file!")

    if len(urls) != 0 and params != "":
        print(f"SQLM command executed: python3 sqlmap.py -u '<url>' {params}")
        for url in urls:
            if url.endswith("\n"):
                url = url[:-1]
            print(f"SQLM output for {url}:")
            proc = subprocess.run(f"cd ~; cd sqlmap-dev; python3 sqlmap.py -u '{url}' {params}", shell=True, capture_output=True)
            print(proc.stdout.decode())


if __name__ == "__main__":
    sqlm_run()
