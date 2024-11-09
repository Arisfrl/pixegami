Here's a `README.md` for your project, tailored to the Python script you provided:

---

# 📝 Task Management API Script

This project is a Python-based utility for interacting with the Pixegami task management API. The script includes functions to create, update, retrieve, list, and delete tasks via HTTP requests. It also contains a set of automated test cases to validate the functionality of each API endpoint.

## 📋 Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Testing](#testing)
6. [Project Structure](#project-structure)
7. [Contributing](#contributing)
8. [License](#license)

## ✨ Features
- **Create a Task**: Adds a new task for a user.
- **Update a Task**: Updates the content and status of an existing task.
- **Retrieve a Task**: Fetches details of a specific task.
- **List Tasks**: Retrieves all tasks for a specific user.
- **Delete a Task**: Deletes a task by its ID.
- **Automated Testing**: Includes test cases to ensure the API endpoints work as expected.

## 🔧 Requirements
- Python 3.x
- `requests` library

## 💻 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Arisfrl/pixegami.git
    cd pixegami
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirement.txt
    ```

## 🚀 Usage

To use the script, you can run the various test functions defined in the code. These functions interact with the Pixegami API to perform CRUD (Create, Read, Update, Delete) operations on tasks.

### Example: Creating a Task
You can create a task by calling the `create_task()` function:

```python
payload = {
    "content": "Your task content here",
    "user_id": "example_user",
    "is_done": False
}
response = create_task(payload)
print(response.json())
```

## 🛠️ Testing
This project includes a suite of automated test functions to verify the functionality of the API endpoints.

### Running the Tests
To run all the tests, execute the following command in your terminal:

```bash
pytest -v -s .\test_todo_api.py
```

### Included Test Cases
1. **Test API Endpoint**: `test_can_call_endpoint()` - Verifies if the API is accessible.
2. **Test Task Creation**: `test_create_task()` - Creates a task and checks if it was successfully created.
3. **Test Task Update**: `test_update_task()` - Updates an existing task and verifies the update.
4. **Test Task Listing**: `test_list_users()` - Lists all tasks for a specific user.
5. **Test Task Deletion**: `test_delete_task()` - Deletes a task and checks if it is removed.

### Sample Output
Here's an example of how the output might look:

```bash
test_user_abc123
{
  "task": {
    "task_id": "task_456789",
    "content": "test_content",
    "user_id": "test_user_abc123",
    "is_done": false
  }
}
```

## 🗂️ Project Structure
```
project-root/
├── script.py       # Main Python script
├── README.md       # Documentation
└── requirements.txt # List of dependencies (if necessary)
```

## 🤝 Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
