def test_create_user(client):
    res = client.post("/users/create", json={
        "username": "u1",
        "email": "u1@test.com",
        "password": "123456",
        "full_name": "User One"
    })
    assert res.status_code == 201
    data = res.json()
    assert data["email"] == "u1@test.com"


def test_delete_user(client):
    r = client.post("/users/create", json={
        "username": "u2",
        "email": "u2@test.com",
        "password": "123456",
        "full_name": "User Two"
    })
    uid = r.json()["id"]

    login = client.post("/auth/login", data={
        "username": "u2@test.com",
        "password": "123456"
    })
    token = login.json()["access_token"]

    res = client.delete(
        f"/users/{uid}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert res.status_code == 200
