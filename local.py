import requests

res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "Golang", "videos": 54})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "PHP", "videos": 43})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "C#", "videos": 33})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "A", "videos": 66})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "B", "videos": 34})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "C", "videos": 99})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "D", "videos": 42})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "F", "videos": 10})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "G", "videos": 83})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "H", "videos": 46})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "I", "videos": 87})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "J", "videos": 66})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "K", "videos": 73})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "L", "videos": 37})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "M", "videos": 57})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "N", "videos": 75})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "O", "videos": 15})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "P", "videos": 34})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "Q", "videos": 74})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "R", "videos": 22})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "S", "videos": 35})
res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "T", "videos": 34})
res = requests.get("http://127.0.0.1:3000/api/courses?page=1&on_page=10")



print(res.json())
