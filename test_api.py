import requests

test_counter = 1

# URL Tests
URL_LIST = ["http://127.0.0.1:8000/athletes/bad_page",
            "http://127.0.0.1:8000/athletes/2", "http://127.0.0.1:8000/athletes/id=2",
            "http://127.0.0.1:8000/athletes/fake_param=2", "http://127.0.0.1:8000/athletes/?bad_query=2",
            "http://127.0.0.1:8000/athletes/", "http://127.0.0.1:8000/athletes/?id=6"]

print("*" * 80)
print("URL MANUAL TESTS")
for URL in URL_LIST:
    print("*" * 80)
    print("Manual Test " + str(test_counter) + ":")
    print("URL: " + URL)
    r = requests.get(url=URL)
    print("Status Code: " + str(r.status_code))
    if r.status_code == 200:
        data = r.json()
        print("Response Data: " + str(data))

    test_counter += 1

# Parameter Tests
URL = "http://127.0.0.1:8000/athletes/"

PARAMS_LIST = [{}, {'id': [3]}, {'id': [1, 2, 3, 4]}, {'id': [8, 99]}, {'id': [10]}, {'name': "Bob"}]

print("\n" + "*" * 80)
print("PARAMETERS MANUAL TESTS")
for PARAMS in PARAMS_LIST:
    print("*" * 80)
    print("Manual Test " + str(test_counter) + ":")
    print("URL: " + URL)
    print("Parameters: " + str(PARAMS))
    r = requests.get(url=URL, params=PARAMS)
    print("Status Code: " + str(r.status_code))
    if r.status_code == 200:
        data = r.json()
        print("Response Data: " + str(data))

    test_counter += 1