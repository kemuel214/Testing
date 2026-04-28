def greet(name):
    if not name:
        return "Hello, Stranger!"
    return f"Hello, {name}!"

def greet_all(names):
    for name in names:
        print(greet(name))

def is_valid_name(name):
    return isinstance(name, str) and name.strip() != ""

# Test cases
user_name = "Brendan"
empty_name = ""
none_name = None
space_name = "   "
number_name = 123  # invalid input test

print("Single Greeting Test:")
print(greet(user_name))
print()

print("Edge Cases:")
print(greet(empty_name))
print(greet(none_name))
print(greet(space_name))
print()

print("Batch Greeting Test:")
names_list = ["Anna", "Mark", "", "Luna", "   ", "Eli"]
greet_all(names_list)
print()

print("Validation Test:")
test_inputs = [user_name, empty_name, none_name, space_name, number_name]

for item in test_inputs:
    print(f"Input: {item} -> Valid: {is_valid_name(item)}")