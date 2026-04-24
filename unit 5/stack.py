stack = []

def push(x):
    stack.append(x)

def safe_pop():
    if not stack:
        print("Stack is empty, nothing to pop")
        return None
    return stack.pop()

push(10)
print(safe_pop())