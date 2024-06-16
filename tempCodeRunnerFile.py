import requests
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response = requests.get(f'https://www.ambitionbox.com/list-of-companies?page=1', headers=headers)
print(response.text)
