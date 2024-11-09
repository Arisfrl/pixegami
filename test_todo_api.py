import uuid
import requests

endpoint = "https://todo.pixegami.io"

def create_task(payload):
     return requests.put(endpoint + "/create-task", json=payload)
def update_task(payload):
     return requests.put(endpoint + "/update-task", json=payload)
def get_task(task_id):
     return requests.get(endpoint + f"/get-task/{task_id}")
def list_task(user_id):
     return requests.get(endpoint + f"/list-tasks/{user_id}")
def delete_task(task_id):
     return requests.delete(endpoint + f"/delete-task/{task_id}")
def new_payload():
     user_id = f"test_user_{uuid.uuid4().hex}"
     content = f"test_content_{uuid.uuid4().hex}"
     return {
          "content": content,
          "user_id": user_id,
          "is_done": False,
     }

# res = requests.get(endpoint)
# print(res)
#
# data = res.json()
# print(data)
#
# status_code = res.status_code
# print(status_code)

def test_can_call_endpoint():
     response = requests.get(endpoint)
     assert response.status_code == 200
     pass

def test_create_task():
     payload = new_payload()
     create_task_response = create_task(payload)
     assert  create_task_response.status_code == 200

     data = create_task_response.json()
     print(data)

     task_id = data["task"]["task_id"]
     get_task_response = get_task(task_id)
     assert get_task_response.status_code == 200

     get_task_data = get_task_response.json()
     print(get_task_data)
     assert get_task_data["content"] == payload["content"]
     assert get_task_data["user_id"] == payload["user_id"]
     # to check failure
     # assert get_task_data["user_id"] == "Wrong user id"

def test_update_task():
     # create a task
     payload = new_payload()
     create_task_res = create_task(payload)
     assert create_task_res.status_code == 200
     task_id = create_task_res.json()["task"]["task_id"]
     # update the task
     update_payload = {
          "content": "Update Content",
          "user_id": payload["user_id"],
          "task_id": task_id,
          "is_done": False,
     }
     update_task_res = update_task(update_payload)
     assert update_task_res.status_code == 200
     # get and validate the changes
     get_task_res = get_task(task_id)
     assert get_task_res.status_code == 200
     assert get_task_res.json()["content"] == update_payload["content"]
     assert get_task_res.json()["user_id"] == payload["user_id"]
     pass

def test_list_users():
     # Create N task
     n = 3
     payload = new_payload()
     user_id = payload["user_id"]
     print(user_id)
     for _ in range(n):
         create_task_res = create_task(payload)
         assert create_task_res.status_code == 200

     # List task, and check that there are N items.
     list_task_res = list_task(user_id)
     assert list_task_res.status_code == 200
     data = list_task_res.json()
     tasks = data["tasks"]
     assert len(tasks) == n
     pass

def test_delete_task():
     # create task.
     payload = new_payload()
     create_task_res = create_task(payload)
     print(create_task_res.json())
     print(create_task_res.status_code)
     assert create_task_res.status_code == 200
     task_id = create_task_res.json()["task"]["task_id"]
     # delete task.
     delete_task_res = delete_task(task_id)
     print(delete_task_res.status_code)
     assert delete_task_res.status_code == 200
     # get task and check task is not found.
     get_task_res = get_task(task_id)
     print(get_task_res.status_code)
     assert get_task_res.status_code == 404
     pass
