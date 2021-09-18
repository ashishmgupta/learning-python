
# make a get request to "http://api.open-notify.org/iss-now.json"
# Print the response
# Get the status codes for 200, 404 and 500 and return the user friendly response accordingly

import requests
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
print(response.text)


if response.status_code == 200:
    print("success")
elif response.status_code == 404:
    print("not found")
elif response.status_code == 500:
    print("error")
else:
    print("something else")

json_data = response.json()
#{
#    "message": "success", 
#    "iss_position": 
#        {
#            "longitude": "-175.0542", 
#            "latitude": "-47.2320"
#        }, 
#    "timestamp": 1631994177
#}

print(json_data["message"])
print(json_data["iss_position"]["latitude"])
print(json_data["iss_position"]["longitude"])
print(json_data["timestamp"])
print(len(json_data))
