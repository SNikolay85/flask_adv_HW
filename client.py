import requests

# response = requests.post('http://127.0.0.1:8000/advertisements/',
#             json={'header': 'adv_2', 'description': 'text_1', 'user': 'user_1'})


# response = requests.patch('http://127.0.0.1:8000/advertisements/user_2/2',
#                          json={'header': 'adv_2',
#                                'description': 'text_2',
#                                'user': 'user_2'})

# response = requests.patch('http://127.0.0.1:8000/advertisements/3',
#                          json={'description': 'adv_1 text_2'})
# print(response.status_code)
# print(response.text)

response = requests.delete("http://127.0.0.1:8000/advertisements/user_2/2")

print(response.status_code)
print(response.text)

response = requests.get("http://127.0.0.1:8000/advertisements/1")

print(response.status_code)
print(response.text)


response = requests.get("http://127.0.0.1:8000/advertisements/2")

print(response.status_code)
print(response.text)
