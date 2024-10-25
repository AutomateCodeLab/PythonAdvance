# 1. Implementation of a Stack using a List
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

# 2. Implementation of a Queue using Collections.deque
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return "Queue is empty!"

    def is_empty(self):
        return len(self.queue) == 0

# 3. Singly Linked List Node and Operations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 4. Binary Search Algorithm (for a sorted list)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 5. Quick Sort Algorithm (Sorting Technique using Recursion)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 6. Recursive Function to Find Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Testing the Program
if __name__ == "__main__":
    # Stack Operations
    print("=== Stack Operations ===")
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print(f"Pop from stack: {stack.pop()}")

    # Queue Operations
    print("\n=== Queue Operations ===")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(f"Dequeue from queue: {queue.dequeue()}")

    # Linked List Operations
    print("\n=== Linked List Operations ===")
    linked_list = LinkedList()
    linked_list.insert_at_head(5)
    linked_list.insert_at_head(10)
    linked_list.display()

    # Binary Search
    print("\n=== Binary Search ===")
    arr = [1, 3, 5, 7, 9, 11]
    target = 5
    result = binary_search(arr, target)
    print(f"Element {target} found at index: {result}")

    # Quick Sort
    print("\n=== Quick Sort ===")
    unsorted_arr = [3, 6, 8, 10, 1, 2, 1]
    sorted_arr = quick_sort(unsorted_arr)
    print(f"Sorted Array: {sorted_arr}")

    # Recursive Factorial
    print("\n=== Recursive Factorial ===")
    n = 5
    print(f"Factorial of {n} is: {factorial(n)}")
