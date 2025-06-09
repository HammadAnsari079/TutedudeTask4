user_input = input("Enter some text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")


more_input = input("Enter more text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(more_input + "\n")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)