# Author : Ashish Gupta
# Registers specificed number of users in the JuiceShop application [https://owasp.org/www-project-juice-shop/]
# This can be used as baseline for how users get created in the JuiceShop application.
# Ideally this pattern should be learnt by a WAF product. So if there is an anomaly in the request, WAF can recognize and alert.

# TODO :
#   a) Renerate the prefix of the email address instead of asking the user.
#   b) Remove hardcoding of values in the request payload.
#   c) Add exception handling
import requests
import json
url = ""
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
user_prefix = ""

# TODO : Renerate the prefix of the email address instead of asking the user
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def generate_payload(counter):
    email = user_prefix+str(counter)+"@example.com"
    data = {
        "email":email,
        "password":"password",
        "passwordRepeat":"password",
        "securityQuestion":
            {
                "id":str(counter),
                "question":"Mother's maiden name?",
                "createdAt":"2021-09-21T18:06:00.509Z",
                "updatedAt":"2021-09-21T18:06:00.509Z",
                "lastLoginIp":"8.8.8.8"
            },
        "securityAnswer":"test"
    }

    jsonObject = json.dumps(data)
    return jsonObject

def create_users(number_of_users):
    print(f'Number of users to be created {number_of_users}')
    for x in range(0, number_of_users-1):
        jsonObject = generate_payload(x)
        print(jsonObject)
        response = requests.post(url=url, data=jsonObject, headers=headers)
        print(response.status_code)
        response.raise_for_status()
        if response.status_code == 201:
            response_json = response.json()
            #print("User " + str(response_json["email"]) + " created successfully!")
            print(response.text)

url = input("Enter your JuiceShop application URL : ")
url += "/api/Users"
print(url)
user_prefix = input("Enter the prefix of the user email address so It can suffix with an incremental number.\n e.g. If you supply \"user\", users created will be user_1@example.com, user_2@example.com and so on...\n Enter the prefix now : ")
number_of_users = int(input("Enter the number of users to be created : "))
create_users(number_of_users)
