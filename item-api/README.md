# FastAPI CRUD API

A simple RESTful CRUD API built with FastAPI, following a structured architecture with separation of concerns.

## Project Structure

```
my_fastapi_app/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── item_routes.py  # API routes for items
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py        # App configuration
│   ├── models/
│   │   ├── __init__.py      
│   │   └── item_model.py    # Pydantic models
│   ├── services/
│   │   ├── __init__.py
│   │   └── item_service.py  # Business logic
│   └── repositories/
│       ├── __init__.py
│       └── item_repository.py # Data access layer
├── tests/
│   ├── __init__.py
│   └── test_items.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/my-fastapi-app.git
cd my-fastapi-app
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install fastapi uvicorn pydantic-settings
```

4. Run the application
```bash
python -m app.main
```

The API will be available at `http://localhost:8000`

## API Documentation

After starting the application, you can access the interactive API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/v1/items/ | Create a new item |
| GET | /api/v1/items/ | Get all items |
| GET | /api/v1/items/{item_id} | Get a specific item |
| PUT | /api/v1/items/{item_id} | Update an item |
| DELETE | /api/v1/items/{item_id} | Delete an item |

## Testing the API with cURL

### Create an item
```bash
curl -X POST "http://localhost:8000/api/v1/items/" -H "Content-Type: application/json" -d '{
  "name": "Test Item",
  "description": "This is a test item",
  "price": 19.99
}'
```

### Get all items
```bash
curl -X GET "http://localhost:8000/api/v1/items/"
```

### Get a specific item
```bash
curl -X GET "http://localhost:8000/api/v1/items/your-item-id-from-the-response"
```

### Update an item
```bash
curl -X PUT "http://localhost:8000/api/v1/items/your-item-id-from-the-response" -H "Content-Type: application/json" -d '{
  "name": "Updated Item",
  "description": "This item has been updated",
  "price": 29.99
}'
```

### Delete an item
```bash
curl -X DELETE "http://localhost:8000/api/v1/items/your-item-id-from-the-response"
```

## Key Features

- **Structured Architecture**: Clear separation of concerns with repositories, services, and API routes
- **Well-Defined Models**: Using Pydantic for data validation
- **RESTful Design**: Following REST principles for API design
- **Dependency Injection**: Leveraging FastAPI's dependency injection system
- **Automatic Documentation**: Interactive API documentation with Swagger and ReDoc

## Future Enhancements

- [ ] Add database integration (SQLAlchemy)
- [ ] Implement authentication and authorization
- [ ] Add comprehensive testing
- [ ] Implement pagination for list endpoints
- [ ] Add filtering and sorting capabilities

## License

This project is licensed under the MIT License - see the LICENSE file for details.