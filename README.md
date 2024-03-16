# Flask Backend API for Contact Management

This project provides a simple backend API built with Flask (Python) for managing a contact list. Contact information is stored in a JSON file (contact.json) and loaded upon application startup. The API offers functionalities to:

- Get a specific contact by ID
- Add new contact
- Delete a specific contact by ID

## Features

- JSON Data Storage: Leverages a JSON file (contact.json) for data persistence (easily modifiable).
- Comprehensive Logging: Logs all API requests to app.log for monitoring and debugging (excluding sensitive information).
- Basic Validation: Ensures data integrity through basic validation checks( including formats of email and phone number).
- Test-Driven Development: Includes test cases to ensure functionality and reliability of endpoints.

## Endpoints

### GET /contacts/<contact_id>

Get contact information(name, email, and phone number) based on ID.

**Parameters**

| Name | Required | Type | Description |
| ----:|:--------:|:----:| ----------- |
| `contact_id` | required | string | The ID of the contact stored in our contact list. |

**Response**
```json
// Contact not found
{
  "error": "Contact not found"
}

or

// Contact found
{
  "data": {
    "_id": "5867c016-380a-48a8-8972-a3df1b26b899", // same as contact_id
    "email": "wattshammond@gogol.com",
    "name": "Watts Hammond",
    "phone_number": "+6585859239"
  }
}
```

### POST /contacts

Add contact information(name, email, and phone number) into our contact list.

**Body (JSON)**
| Name | Required | Type | Description |
| ----:|:--------:|:----:| ----------- |
| `name` | required | string | The name of the contact to store into our contact list. |
| `email` | required | string | The unique email address of the contact to store into our contact list. |
| `phone_number` | required | string | The unique Singapore phone number(inclusive of "+65") of the contact to store into our contact list. |

**Response**

```json
// Empty request body
{
  "error": "Empty request body"
}

or

// Missing required fields(name, email, and  phone_number)
{
  "error": "Missing required fields"
}

or

// Invalid email format
{
  "error": "Invalid email format"
}

or

// Invalid phone number format
{
  "error": "Invalid phone number format"
}

or

// Email or phone_number existed
{
  "error": "Email or phone_number existed"
}

or

// Added contact
{
  "message": "Added contact with ID: ID5867c016-380a-48a8-8972-a3df1b26b899",
}
```

### DELETE /contacts/<contact_id>

Delete stored contact information based on ID.

**Parameters**
| Name | Required | Type | Description |
| ----:|:--------:|:----:| ----------- |
| `contact_id` | required | string | The ID of the contact stored in our contact list. |

**Response**

```json
// Contact not found
{
  "error": "Contact not found"
}

or

// Deleted contact
{
  "message": "Deleted contact with ID: 5867c016-380a-48a8-8972-a3df1b26b899", // same as contact_id
}
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/Pyrolf/contact-backend-api-python-flask.git
```

Go to the project directory

```bash
  cd contact-backend-api-python-flask
```

Install dependencies

```bash
    pip install -r requirements. txt
```

Start the server

```bash
  python -m flask run
```

## Running Tests

To run tests, run the following command

```bash
  python -m pytest
```

## Live

Deployed and hosted using Koyeb at <https://contact-api-pyrolf.koyeb.app/>
