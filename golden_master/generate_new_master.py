import requests


def generate_master():
    url = "http://localhost/api/prescriptions/{}"
    cookies = requests.post("http://localhost/auth/api/login",
                            json={'username': 'root', 'password': 'password'}).cookies
    with open('golden_master.txt', 'w') as f:
        for location in range(1, 61):
            f.write(f"Location ID: {location}:\n")
            res = requests.get(url.format(location), cookies=cookies)
            f.write(res.text)


if __name__ == '__main__':
    generate_master()
