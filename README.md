Title: Random Task Selection

Difficulty: Medium

Description:

You are given a set of tasks, each with an associated probability of occurrence. Your task is to implement a class TaskSelector that supports two operations:

Constructor: TaskSelector(tasks: List[Tuple[str, float]]) - Initializes the task selector with a list of tasks, where each task is represented by a tuple (name, probability), where name is a string representing the task name and probability is a float representing the probability of occurrence of the task. The probabilities are guaranteed to be valid and sum up to 1.

Method: select_task() -> str - Returns the name of a randomly selected task based on the provided probabilities.

You need to implement the TaskSelector class and ensure that the selected task is chosen randomly but with probabilities consistent with the provided probabilities.

Constraints:

The number of tasks is at most 10^4.
The length of task names is at most 100.
The probability values are between 0 and 1, inclusive.
