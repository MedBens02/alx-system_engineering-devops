#!/usr/bin/python3
"""for a given employee ID, returns TODO list progress."""
import requests
import sys

if __name__ == "__main__":
	RESTAPI = "https://jsonplaceholder.typicode.com/"
	requestID = sys.argv[1]
	user = requests.get(RESTAPI + "users/{}".format(requestID)).json()
	todo_list = requests.get(RESTAPI + "todos", params={"userId": requestID}).json()

	completed_tasks = [t.get("title") for t in todo_list if t.get("completed") is True]
	print("Employee {} is done with tasks({}/{}):".format(
		user.get("name"), len(completed_tasks), len(todo_list)))
	[print("\t {}".format(c)) for c in completed_tasks]
