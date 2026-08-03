# Caesar Cipher - decrypting with a key
def check_int(prompt, value_min, value_max):
    while True:
        try:
            x = int(input(prompt))
            if value_min <= x <= value_max:
                return x
            print(f"Error! Enter a value between {value_min} and {value_max}.")
        except ValueError:
            print("Error! Enter only integers.")

def check_string(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input is empty")
            continue
        return user_input

# Main Program Execution
text = check_string("Enter your message: ")
cipher = ''
shift_value = check_int("Enter the cipher shift range: ", 1, 25)

for char in text:
    if not char.isalpha():
        cipher += char
    else:
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        position = ord(char) - first
        shifted_position = position - shift_value
        wrapped_position = shifted_position % 26
        code = first + wrapped_position
        cipher += chr(code)

print("Encrypted message:", cipher)
