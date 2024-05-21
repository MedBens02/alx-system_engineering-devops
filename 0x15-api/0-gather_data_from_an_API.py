#!/usr/bin/python3
"""For a given employee ID, returns TODO list progress."""
from requests import get
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    user = get("https://jsonplaceholder.typicode.com/users/{}"
               .format(userId))

    name = user.json().get('name')

    todo_list = get('https://jsonplaceholder.typicode.com/todos')
    AllTasks = 0
    completedTasks = 0

    for todo in todo_list.json():
        if todo.get('userId') == int(userId):
            AllTasks += 1
            if todo.get('completed'):
                completedTasks += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completedTasks, AllTasks))

    print('\n'.join(["\t " + task.get('title') for task in todo_list.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
