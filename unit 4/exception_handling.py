try:
    f = open(input(), "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission")
