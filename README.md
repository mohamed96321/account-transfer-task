# account-transfer-task
## Follow these instructions to run project:
### python3 -m venv env
### env/Scripts/activate (Windows) or `source env/Scripts/activate` (Linux)
### pip install django djangorestframework
### python manage.py makemigrations accounts
### python manage.py migrate
### python manage.py runserver
`**API Endpoints:**
```
{
            "name": "Import Accounts",
            "request": {
                "method": "POST",
                "header": [],
                "body": {
                    "mode": "formdata",
                    "formdata": [
                        {
                            "key": "file",
                            "type": "file",
                            "src": ""
                        }
                    ]
                },
                "url": {
                    "raw": "http://127.0.0.1:8000/api/accounts/import_accounts/",
                    "protocol": "http",
                    "host": ["127", "0", "0", "1"],
                    "port": "8000",
                    "path": ["api", "accounts", "import_accounts"]
                }
            }
        },
        {
            "name": "List Accounts",
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "http://127.0.0.1:8000/api/accounts/",
                    "protocol": "http",
                    "host": ["127", "0", "0", "1"],
                    "port": "8000",
                    "path": ["api", "accounts"]
                }
            }
        },
        {
            "name": "Get Account Info",
            "request": {
                "method": "GET",
                "header": [],
                "url": {
                    "raw": "http://127.0.0.1:8000/api/accounts/{id}/",
                    "protocol": "http",
                    "host": ["127", "0", "0", "1"],
                    "port": "8000",
                    "path": ["api", "accounts", "{id}"]
                }
            }
        },
        {
            "name": "Transfer Funds",
            "request": {
                "method": "POST",
                "header": [],
                "body": {
                    "mode": "raw",
                    "raw": "{\n    \"to_account_id\": \"be6acfdc-cae1-4611-b3b2-dfb5167ba5fe\",\n    \"amount\": 1000\n}",
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": {
                    "raw": "http://127.0.0.1:8000/api/accounts/{id}/transfer/",
                    "protocol": "http",
                    "host": ["127", "0", "0", "1"],
                    "port": "8000",
                    "path": ["api", "accounts", "{id}", "transfer"]
                }
            }
        }
```
