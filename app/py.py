import requests

response = requests.post("https://example.com/referral", json={"fake_data": "referral_success"})
print(response.text)
