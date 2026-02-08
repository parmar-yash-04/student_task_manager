def test_login_success(client):
    client.post("/users/create", json={
        "username": "auth1",
        "email": "auth@test.com",
        "password": "123456",
        "full_name": "Auth User"
    })

    res = client.post("/auth/login", data={
        "username": "auth@test.com",
        "password": "123456"
    })

    assert res.status_code == 200
    assert "access_token" in res.json()


def test_login_fail(client):
    res = client.post("/auth/login", data={
        "username": "wrong@test.com",
        "password": "bad"
    })
    assert res.status_code == 403