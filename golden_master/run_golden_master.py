from unittest import TestCase

import requests


def generate_current_output():
    url = "http://localhost/api/prescriptions/{}"
    cookies = requests.post("http://localhost/auth/api/login",
                            json={'username': 'root', 'password': 'password'}).cookies
    with open('current_run.txt', 'w') as f:
        for location in range(1, 61):
            f.write(f"Location ID: {location}:\n")
            res = requests.get(url.format(location), cookies=cookies)
            f.write(res.text)


class TestGoldenMaster(TestCase):
    def test_golden_master(self):
        generate_current_output()
        with open('golden_master.txt', 'r') as master:
            with open('current_run.txt', 'r') as current:
                expected = master.readlines()
                actual = current.readlines()
                self.assertEqual(expected, actual)


if __name__ == '__main__':
    test = TestGoldenMaster()
    test.test_golden_master()
