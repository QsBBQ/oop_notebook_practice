import datetime

last_id = 0

class Todo:
    """
    Class represents a Todo/task
    """

    def __init__(self, task, task_due, status="open", tags=""):
        """
        Initialize a Todo
        """
        self.task = task
        self.tags = tags
        self.task_due = task_due
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        self.status = status

    def match(self):
        pass

class TodoList:
    """
    Class represents a collection of todo tasks
    """
    def __init__(self):
        """
        Initialize a todolist
        """
        self.todos = []

    def create_todo(self, task, task_due, status="open", tags=""):
        """
        Create and add a todo to the todolist
        """
        self.todos.append(Todo(task, task_due, status, tags))

    def read_todo(self, todo_id):
        """
        Read/retrieve a todo on id
        """
        for todo in self.todos:
            if str(todo.id) == str(todo_id):
                return todo
        return None

    def update_todo(self, todo_id, task):
        """
        Update todo by ID
        """
        todo = self.read_todo(todo_id)
        if todo:
            todo.task = task
            return True
        return False

    def delete_todo(self, todo_id):
        """
        Delete todo by id from todos
        """
        todo = self.read_todo(todo_id)
        if todo:
            # self.todos.remove(todo)
            todo_index = self.todos.index(todo)
            del self.todos[todo_index]
            return True
        return False
