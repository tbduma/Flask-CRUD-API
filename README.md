# Flask CRUD API - Backend and API Development

This project contains a Flask-based RESTful API for managing product information. The API supports CRUD (Create, Read, Update, Delete) operations, allowing users to add, read, update, and delete product entries.

## Setting Up and Running the Project

Follow the steps below to set up and run the project on your local machine.

### Requirements

- Python 3.x
- Flask
- Flask-CORS (to handle CORS issues)

### Installation Steps

1. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/tbduma/Flask-CRUD-API.git
    cd Flask-CRUD-API
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate  # Windows
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

5. Verify the server is running:
   - Open a browser or Postman and go to `http://127.0.0.1:5000`.
   - The API should be working correctly.

### API Endpoints and Usage

Below are the CRUD operations and how to interact with them.

#### POST: Add a Product
- **URL:** `http://127.0.0.1:5000/products`
- **HTTP Method:** `POST`
- **Body (JSON):**

```json
{
  "id": "1",
  "info": {
    "name": "Playstation 5",
    "price": 499.90
  }
}

#### Success Response:
- **HTTP Status Code:** 201 CREATED
- **Response:**

```json
{
  "message": "Product added successfully!"
}

GET: Retrieve a Product

	•	URL: http://127.0.0.1:5000/products/1
	•	HTTP Method: GET
	•	Success Response:
	•	HTTP Status Code: 200 OK
	•	Response:
{
  "id": "1",
  "info": {
    "name": "Playstation 5",
    "price": 499.90
  }
}

PUT: Update a Product

	•	URL: http://127.0.0.1:5000/products/1
	•	HTTP Method: PUT
	•	Body (JSON):
{
  "info": {
    "name": "Playstation 5",
    "price": 699.90
  }
}

	•	Success Response:
	•	HTTP Status Code: 200 OK
	•	Response:
{
  "message": "Product updated successfully!"
}

DELETE: Delete a Product

	•	URL: http://127.0.0.1:5000/products/1
	•	HTTP Method: DELETE
	•	Success Response:
	•	HTTP Status Code: 200 OK
	•	Response:
{
  "message": "Product deleted successfully!"
}

##Error Handling and Response Formats

The API handles errors with appropriate HTTP status codes and messages. For example:

	•	If a product is not found:
	•	HTTP Status Code: 404 Not Found
	•	Response: {"message": "Product not found"}

Project Structure

	•	main.py: The main API application file.
	•	venv/: Files for the virtual environment.
	•	requirements.txt: List of required Python packages.

This information should help you set up, run, and test the API using Postman.
