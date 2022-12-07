import requests

res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "Golang", "videos": 54})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "PHP", "videos": 43})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "C#", "videos": 33})
res = requests.delete("http://127.0.0.1:3000/api/courses/2")
print(res.json())