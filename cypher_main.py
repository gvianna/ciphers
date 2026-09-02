from utils.validation import check_int, check_string
from algorithms.ciphers import caesar_cipher, atbash_cipher


def get_input_encrypt():
    text = check_string("Enter your message to encrypt: ")
    shift_value = check_int("Enter the cipher shift range (1-25): ", 1, 25)
    return text, shift_value


def get_input_decrypt():
    text = check_string("Enter your message to decrypt: ")
    shift_value = check_int("Enter the cipher shift range (1-25): ", 1, 25)
    return text, -shift_value


def get_input_crack():
    return check_string("Enter your message: ")


def caesar_crack(text):
    results = []

    for shift in range(1, 26):
        decrypted = caesar_cipher(text, -shift)
        results.append((shift, decrypted))

    return results


def get_input_atbash():
    text = check_string("Enter your message: ")
    return text


def main():
    print("cheguei no menu")
    while True:
        print("\n" + "═" * 33)
        print("🔐 CIPHER TOOL 🔐".center(30, "-"))
        print("═" * 33)
        print("MAIN MENU".center(32, " "))
        print("  [1]  Caesar Encrypt 🔒")
        print("  [2]  Caesar Decrypt 🔓")
        print("  [3]  Crack Caesar Cipher ⚡ ")
        print("  [4]  Atbash Encrypt/Decrypt ")
        print("  [5]  Exit ❌")
        print("═" * 33)

        choice = check_int("👉 Choose an option [1-5]: ", 1, 5)

        if choice == 1:
            print("\n[🔒] Running Caesar Encrypt...")

            text, shift = get_input_encrypt()

            encrypted_message = caesar_cipher(text, shift)

            print("\nEncrypted message:")
            print(encrypted_message)

        elif choice == 2:
            print("\n[🔓] Running Caesar Decrypt...")

            text, shift = get_input_decrypt()

            decrypted_message = caesar_cipher(text, shift)

            print("\nDecrypted message:")
            print(decrypted_message)

        elif choice == 3:
            print("\n[⚡] Cracking Caesar Cipher...")

            text = get_input_crack()

            results = caesar_crack(text)

            for shift, message in results:
                print(f"[{shift:02}] {message}")

        elif choice == 4:
            print("\nRunning Atbash algorithm...")

            text = get_input_atbash()

            result_message = atbash_cipher(text)

            print(f"\n Atbash message: {result_message}")

        elif choice == 5:
            print("\n👋 Exiting Cipher Tool. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
