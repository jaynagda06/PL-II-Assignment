from collections import deque

q = deque()

def enqueue(x):
    q.append(x)

def safe_dequeue():
    if not q:
        print("Queue is empty, cannot dequeue")
        return None
    return q.popleft()

enqueue(5)
print(safe_dequeue())