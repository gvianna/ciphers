# Caesar Cipher - encrypt
# Caesar encryption adds the shift; decryption uses the inverse shift
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


# Atbash Cipher
def atbash_cipher(text: str) -> str:
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
            atbash_position = (25 - position) % 26
            code = first + atbash_position
            cipher += chr(code)

    return cipher
