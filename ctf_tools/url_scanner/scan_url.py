import requests


def scan_url():
    with open("in.txt", "r") as f:
        urls = f.readlines()

    with open("key.txt", "r") as f:
        keyword = f.read()

    if len(urls) == 0:
        print("Enter at least one url to the in.txt file!")
    if keyword == "":
        print("Enter the keyword to the key.txt file!")

    if len(urls) != 0 and keyword != "":
        count_success_html_scans = 0
        count_success_robots_found = 0
        for url in urls:
            if url.endswith("\n"):
                url = url[:-1]
            req = requests.get(url=url)
            if url.endswith("/"):
                req1 = requests.get(url=f"{url}robots.txt")
            else:
                req1 = requests.get(url=f"{url}/robots.txt")
            if req1.status_code == 200:
                print(f"{url} has a robots.txt file!")
                count_success_robots_found += 1
            if keyword in req.text:
                print(f"Keyword found in {url}'s HTML. Possible flag: {req.text[req.text.find(keyword):req.text.find("-->", req.text.find(keyword))]}")
                count_success_html_scans += 1

        if count_success_html_scans == 0:
            print(f"{keyword} wasn't found in any of the input urls!")
        if count_success_robots_found == 0:
            print("robots.txt wasn't found in any of the input urls!")


if __name__ == "__main__":
    scan_url()
