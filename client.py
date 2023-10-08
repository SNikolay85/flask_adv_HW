import requests

response = requests.post('http://127.0.0.1:8000/advertisements/',
            json={'header': 'adv_1', 'description': 'adv_1 text_1', 'user': 'user_1'})


# response = requests.patch('http://127.0.0.1:8000/users/1',
#                          json={'name': 'user_1'})
#
print(response.status_code)
print(response.text)

# response = requests.delete("http://127.0.0.1:8000/advertisements/1")
#
# print(response.status_code)
# print(response.text)

response = requests.get("http://127.0.0.1:8000/advertisements/3")

print(response.status_code)
print(response.text)
