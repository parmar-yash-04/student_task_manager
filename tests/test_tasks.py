def create_user_and_token(client):
    client.post("/users/create", json={
        "username": "taskuser",
        "email": "task@test.com",
        "password": "123456",
        "full_name": "Task User"
    })

    login = client.post("/auth/login", data={
        "username": "task@test.com",
        "password": "123456"
    })

    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    return headers

def test_create_task(client):
    headers = create_user_and_token(client)

    res = client.post("/tasks/create",
        json={"title": "T1", "description": "D1", "priority": 1},
        headers=headers
    )

    assert res.status_code == 201
    assert res.json()["title"] == "T1"

def test_get_single_task(client):
    headers = create_user_and_token(client)

    r = client.post("/tasks/create",
        json={"title": "T2", "description": "D2", "priority": 1},
        headers=headers
    )

    tid = r.json()["id"]

    res = client.get(f"/tasks/{tid}", headers=headers)
    assert res.status_code == 200
    assert res.json()["id"] == tid

def test_update_task(client):
    headers = create_user_and_token(client)

    r = client.post("/tasks/create",
        json={"title": "Old", "description": "D", "priority": 1},
        headers=headers
    )

    tid = r.json()["id"]

    res = client.put(
        f"/tasks/{tid}",
        json={"title": "New"},
        headers=headers
    )

    assert res.status_code == 201
    assert res.json()["title"] == "New"

def test_delete_task(client):
    headers = create_user_and_token(client)

    r = client.post("/tasks/create",
        json={"title": "Del", "description": "D", "priority": 1},
        headers=headers
    )

    tid = r.json()["id"]

    res = client.delete(f"/tasks/{tid}", headers=headers)
    assert res.status_code == 200