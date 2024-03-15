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
    assert "Added contact with ID:" in response.json["message"]