def test_add_contact_empty_request_body(client):
    response = client.post("/contacts",
                           json={})
    assert response.status_code == 400
    assert response.json["error"] == "Empty request body"

def test_add_contact_missing_name(client):
    response = client.post("/contacts",
                           json={
                               "email": "test@email.com",
                               "phone_number": "+6588888888"
                           })
    assert response.status_code == 400
    assert response.json["error"] == "Missing required fields"

def test_add_contact_missing_email(client):
    response = client.post("/contacts",
                           json={
                               "name": "Test User",
                               "phone_number": "+6588888888"
                           })
    assert response.status_code == 400
    assert response.json["error"] == "Missing required fields"

def test_add_contact_missing_phone_number(client):
    response = client.post("/contacts",
                           json={
                               "name": "Test User",
                               "email": "test@email.com"
                           })
    assert response.status_code == 400
    assert response.json["error"] == "Missing required fields"

def test_add_contact_invalid_email_format(client):
    response = client.post("/contacts",
                           json={
                               "name": "Test User",
                               "email": "invalid_email.com",
                               "phone_number": "+6588888888"
                           })
    assert response.status_code == 400
    assert response.json["error"] == "Invalid email format"

def test_add_contact_invalid_phone_number_format(client):
    response = client.post("/contacts",
                           json={
                               "name": "Test User",
                               "email": "test@email.com",
                               "phone_number": "+658888888"
                           })
    assert response.status_code == 400
    assert response.json["error"] == "Invalid phone number format"

def test_add_contact_email_existed(client):
    response = client.post("/contacts",
                           json={
                               "name": "Test User",
                               "email": "exist@user.com",
                               "phone_number": "+6588888888"
                           })
    assert response.status_code == 400
    assert response.json["error"] == "Email or phone_number existed"

def test_add_contact_phone_number_existed(client):
    response = client.post("/contacts",
                           json={
                               "name": "Test User",
                               "email": "test@email.com",
                               "phone_number": "+6599999999"
                           })
    assert response.status_code == 400
    assert response.json["error"] == "Email or phone_number existed"

def test_add_contact_success(client):
    response = client.post("/contacts",
                           json={
                               "name": "Test User",
                               "email": "test@email.com",
                               "phone_number": "+6588888888"
                           })
    assert response.status_code == 200
    assert "Added contact with ID: " in response.json["message"]

def test_get_contact_not_found(client):
    response = client.get("/contacts/not-found")
    assert response.status_code == 404
    assert response.json["error"] == "Contact not found"

def test_get_contact_success(client):
    response = client.get("/contacts/5867c016-380a-48a8-8972-a3df1b26b899")
    assert response.status_code == 200
    assert response.json['data'] == {
        "_id": "5867c016-380a-48a8-8972-a3df1b26b899",
        "name": "Existed User",
        "email": "exist@user.com",
        "phone_number": "+6599999999"
    }

def test_delete_contact_not_found(client):
    response = client.delete("/contacts/not-found")
    assert response.status_code == 404
    assert response.json["error"] == "Contact not found"

def test_get_contact_success(client):
    id = "5867c016-380a-48a8-8972-a3df1b26b899"
    response = client.delete(f"/contacts/{id}")
    assert response.status_code == 200
    assert f"Deleted contact with ID: {id}" in response.json["message"]