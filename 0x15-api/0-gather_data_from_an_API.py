import sys
import requests

def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Check if request was successful
        user_data = user_response.json()

        # Fetch TODO list data
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()  # Check if request was successful
        todos_data = todos_response.json()

        # Extract employee name
        employee_name = user_data.get('name', 'Unknown')

        # Count completed and total tasks
        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data if todo.get('completed', False))

        # Collect completed tasks titles
        completed_tasks = [todo['title'] for todo in todos_data if todo.get('completed', False)]

        # Print the result in the specified format
        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"     {task}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
