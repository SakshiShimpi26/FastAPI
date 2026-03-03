# ⚡ FastAPI -- High Performance Python APIs

FastAPI is a modern, high-performance web framework for building APIs
with Python 3.8+. It is designed for speed, simplicity, and automatic
validation, making it ideal for production-ready backend systems.

FastAPI is built on top of:

-   Starlette → Handles routing, request/response lifecycle, and ASGI
    support\
-   Pydantic → Provides data validation and parsing using Python type
    hints

------------------------------------------------------------------------

## 🚀 Why FastAPI?

### 1️⃣ Fast to Run

FastAPI is one of the fastest Python frameworks available.

-   Built on ASGI (Asynchronous Server Gateway Interface)
-   Uses Starlette for async request handling
-   Compatible with high-performance servers like Uvicorn

This allows handling thousands of concurrent requests efficiently.

------------------------------------------------------------------------

### 2️⃣ Fast to Code

FastAPI reduces development time significantly.

-   Uses Python type hints
-   Automatic request validation
-   Minimal boilerplate code
-   Built-in interactive documentation

✔ Cleaner code\
✔ Fewer bugs\
✔ Faster development

------------------------------------------------------------------------

## 🏗 Architecture Overview

Traditional frameworks (like Flask):

Client → WSGI → Framework → API Code

FastAPI architecture:

Client → ASGI → Starlette → FastAPI → API Code

### Key Difference:

-   WSGI → Synchronous\
-   ASGI → Asynchronous (supports concurrency, WebSockets, background
    tasks)

------------------------------------------------------------------------

## 🧠 Core Features of FastAPI

### ✅ 1. Automatic Data Validation (Pydantic)

FastAPI uses Pydantic models to validate incoming request data.

-   Validates request body
-   Validates query parameters
-   Enforces data types
-   Returns structured error messages automatically

Example:

``` python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
    disease: str
```

If invalid data is sent → FastAPI automatically returns
`422 Unprocessable Entity`.

------------------------------------------------------------------------

### ✅ 2. Automatic API Documentation

FastAPI auto-generates:

-   Swagger UI → `/docs`
-   ReDoc → `/redoc`

No extra configuration required.

------------------------------------------------------------------------

### ✅ 3. Type Hint Based Development

``` python
@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    return {"id": patient_id}
```

-   Automatically validates `patient_id` as integer\
-   Generates documentation from type hints\
-   Improves IDE support

------------------------------------------------------------------------

### ✅ 4. Query Parameters & Path Parameters

``` python
@app.get("/patients/{patient_id}")
def get_patient(patient_id: int, active: bool = True):
    return {"id": patient_id, "active": active}
```

-   Path parameters → Required identifiers\
-   Query parameters → Optional filters

------------------------------------------------------------------------

### ✅ 5. Async Support

FastAPI supports both:

``` python
def sync_function():
```

and

``` python
async def async_function():
```

This makes it ideal for:

-   Database operations\
-   ML inference APIs\
-   External API calls\
-   High-concurrency systems

------------------------------------------------------------------------

## 📂 Project Structure

1.  Basics\
2.  Path and Query Parameters\
3.  POST\
4.  PUT\
5.  DELETE

------------------------------------------------------------------------

## 🏥 Example Implemented (Patient Management API)

To demonstrate FastAPI concepts, a simple Patient CRUD API was
implemented:

-   ➕ Create Patient (POST)
-   📖 Get Patient (GET)
-   ✏ Update Patient (PUT)
-   ❌ Delete Patient (DELETE)

Concepts Covered:

-   Path parameters\
-   Query parameters\
-   Request body validation using Pydantic\
-   CRUD operations\
-   Proper HTTP status handling

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3.10+
-   FastAPI
-   Pydantic
-   Uvicorn

------------------------------------------------------------------------

## ▶ How to Run

``` bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Open in browser:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 🎯 Conclusion

FastAPI combines:

⚡ High performance (ASGI)\
🧠 Intelligent validation (Pydantic)\
📄 Automatic documentation\
🧩 Clean type-driven development

It is especially powerful for:

-   ML/AI APIs\
-   Production backend services\
-   Microservices\
-   High-concurrency applications

------------------------------------------------------------------------

⭐ If you found this helpful, feel free to explore and extend the
project!
