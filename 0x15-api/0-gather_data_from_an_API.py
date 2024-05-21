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
    completed = 0

    for task in todo_list.json():
        if task.get('userId') == int(userId):
            AllTasks += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, AllTasks))

    print('\n'.join(["\t " + task.get('title') for task in todo_list.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
