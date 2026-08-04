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

def caesar_cipher(text: str, shift_value: int) -> str:
    cipher = ""
    for char in text:
        if not char.isalpha():
            cipher += char
        else:
            if char.isupper():
                first = ord("A")
            else:
                first = ord("a")
            position = ord(char) - first
            shifted_position = position + shift_value
            wrapped_position = shifted_position % 26
            code = first + wrapped_position
            cipher += chr(code)
    return cipher

# Main Program Execution
text = check_string("Enter your message: ")
shift_value = check_int("Enter the cipher shift range: ", 1, 25)
encrypted_message = caesar_cipher(text, shift_value)
print(encrypted_message)

# Caesar cipher - brute force decryption.
print("--- Brute Force Decryption Mode ---")
brute_text = check_string("Enter the message to decrypt: ")

for shift in range(1, 26):
    # Caesar encryption adds the shift; decryption uses the inverse shift
    decrypted_message = caesar_cipher(brute_text, -shift)
    print(f'[{shift:02}] {decrypted_message}')
