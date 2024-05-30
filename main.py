import random
import json

def normalize_probabilities(tasks):
    total_probability = sum(task['probability'] for task in tasks)
    if total_probability != 1:
        for task in tasks:
            task['probability'] /= total_probability
    return tasks

def get_task(tasks):
    # Create a list of cumulative probabilities
    cumulative_probabilities = []
    cumulative = 0.0
    for task in tasks:
        cumulative += task['probability']
        cumulative_probabilities.append(cumulative)
    
    # Generate a random number and find the corresponding task
    random_value = random.random()
    for i, cumulative_probability in enumerate(cumulative_probabilities):
        if random_value < cumulative_probability:
            return tasks[i]['name']
    return None  # Should never reach here if probabilities are correct

def input_tasks():
    # Input number of tasks
    num_tasks = int(input("Enter the number of tasks (up to 20): "))
    if num_tasks > 20:
        print("The maximum number of tasks is 20.")
        return
    
    tasks = []
    total_probability = 0

    for i in range(num_tasks):
        name = input(f"Enter the name of task {i+1}: ")
        probability = float(input(f"Enter the probability for {name} (as a decimal between 0 and 1): "))
        tasks.append({'name': name, 'probability': probability})
        total_probability += probability

    # Normalize probabilities
    tasks = normalize_probabilities(tasks)
    
    # Save tasks to a file
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
    
    print("\nTasks and their probabilities have been saved.")
    for task in tasks:
        print(f"{task['name']}: {task['probability']:.2%}")

def spin_wheel():
    # Load tasks from a file
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No tasks found. Please input tasks first.")
        return
    
    # Spin the wheel
    task = get_task(tasks)
    print(f"Selected: {task}")

def main():
    while True:
        print("\nMenu:")
        print("1. Input tasks")
        print("2. Spin the wheel")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            input_tasks()
        elif choice == '2':
            spin_wheel()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
