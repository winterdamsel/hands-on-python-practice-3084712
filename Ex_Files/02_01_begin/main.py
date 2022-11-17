RUN_INDENTED = False

message = "running unindented"
print("hello")
if RUN_INDENTED:
    message = "running indented"

print(message)


def my_function():
    greet = "Hello"
    return greet
