import requests

res = requests.post("http://127.0.0.1:3000/api/courses/", {"name": "PHP", "videos": 63})
print(res.json())