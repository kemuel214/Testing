def greet(name):
    if not name:
        return "Hello, Stranger!"
    return f"Hello, {name}!"

user_name = "Josh"
message = greet(user_name)

print(message)