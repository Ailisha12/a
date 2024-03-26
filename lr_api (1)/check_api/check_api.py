import requests



response = requests.post('http://127.0.0.1:3000/api/main',json={'text':"нет воды"})
print(response.text.encode(encoding='utf-8').decode('unicode-escape'))