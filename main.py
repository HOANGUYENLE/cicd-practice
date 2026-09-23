from fastapi import FastAPI

app = FastAPI()


todos = [
    {
        "id": 1,
        "title": "Learn CI/CD",
        "completed": False,
    },
    {
        "id": 2,
        "title": "Learn Docker",
        "completed": False,
    },
]

@app.get("/")
def basic_get():
    return {"message": "Hello"}

@app.get("/todos")
def get_todos():
    return todos


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    return {"message": "Todo not found"}


@app.post("/todos")
def create_todo(title: str):
    new_todo = {
        "id": len(todos) + 1,
        "title": title,
        "completed": False,
    }

    todos.append(new_todo)

    return new_todo


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, completed: bool):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = completed
            return todo

    return {"message": "Todo not found"}


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}

    return {"message": "Todo not found"}