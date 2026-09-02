from utils.validation import check_int, check_string
from algorithms.ciphers import caesar_cipher, atbash_cipher, vigenere_cipher


def get_input_caesar_encrypt():
    text = check_string("Enter your message to encrypt: ")
    shift_value = check_int("Enter the cipher shift range (1-25): ", 1, 25)
    return text, shift_value


def get_input_caesar_decrypt():
    text = check_string("Enter your message to decrypt: ")
    shift_value = check_int("Enter the cipher shift range (1-25): ", 1, 25)
    return text, -shift_value


def get_input_caesar_crack():
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


def get_input_vigenere():
    text = check_string("Enter your message: ")
    key = check_string("Enter your keyword: ")
    return text, key


def show_caesar_about():
    print("\n" + "─" * 42)
    print("ℹ️ ABOUT CAESAR CIPHER ℹ️".center(42))
    print("─" * 42)
    print("• Origin: Ancient Rome (1st Century BC).")
    print("• History: Created by Julius Caesar to protect")
    print("  secret military communications.")
    print("• How it works: Shifts every letter forward by")
    print("  a set number of positions in the alphabet")
    print("  (e.g., with shift 3, 'A' becomes 'D').")
    print("─" * 42)


def show_atbash_about():
    print("\n" + "─" * 42)
    print("ℹ️ ABOUT ATBASH CIPHER ℹ️".center(42))
    print("─" * 42)
    print("• Origin: Ancient Judah (around 500 BC).")
    print("• History: One of the oldest ciphers, originally")
    print("  used in ancient Hebrew texts.")
    print("• How it works: Reverses the alphabet. The first")
    print("  letter becomes the last, second becomes")
    print("  second-to-last ('A' <-> 'Z', 'B' <-> 'Y').")
    print("─" * 42)


def show_vigenere_about():
    print("\n" + "─" * 42)
    print("ℹ️ ABOUT VIGENÈRE CIPHER ℹ️".center(42))
    print("─" * 42)
    print("• Origin: Renaissance Italy (16th Century).")
    print("• History: Named after Blaise de Vigenère.")
    print("  Known for centuries as 'le chiffre indéchiffrable'")
    print("  (the unbreakable cipher).")
    print("• How it works: Uses a repeating keyword where")
    print("  each letter dictates a different Caesar shift")
    print("  for the corresponding message letter.")
    print("─" * 42)


def main():
    while True:
        print("\n" + "═" * 33)
        print("🔐 CIPHER TOOL 🔐".center(30, "-"))
        print("═" * 33)
        print("MAIN MENU".center(32, " "))
        print("  [1]  Caesar Cipher")
        print("  [2]  Atbash Cipher")
        print("  [3]  Vigenère Cipher")
        print("  [4]  Exit ❌")
        print("═" * 33)

        choice = check_int("👉 Choose an option [1-4]: ", 1, 4)

        if choice == 1:
            while True:
                print("\n" + "═" * 33)
                print(" CAESAR CIPHER ".center(30, "-"))
                print("═" * 33)
                print("  [1]  Encrypt 🔒")
                print("  [2]  Decrypt 🔓")
                print("  [3]  Crack ⚡ ")
                print("  [4]  About ℹ️")
                print("  [5]  Back to Main Menu 🔙")
                print("═" * 33)

                caesar_choice = check_int("👉 Choose an option [1-5]: ", 1, 5)

                if caesar_choice == 1:
                    print("\n[🔒] Running Caesar Encrypt...")
                    text, shift = get_input_caesar_encrypt()
                    encrypted_message = caesar_cipher(text, shift)
                    print("\nEncrypted message:")
                    print(encrypted_message)

                elif caesar_choice == 2:
                    print("\n[🔓] Running Caesar Decrypt...")
                    text, shift = get_input_caesar_decrypt()
                    decrypted_message = caesar_cipher(text, shift)
                    print("\nDecrypted message:")
                    print(decrypted_message)

                elif caesar_choice == 3:
                    print("\n[⚡] Cracking Caesar Cipher...")
                    text = get_input_caesar_crack()
                    results = caesar_crack(text)
                    for shift, message in results:
                        print(f"[{shift:02}] {message}")

                elif caesar_choice == 4:
                    show_caesar_about()

                elif caesar_choice == 5:
                    break

        elif choice == 2:
            while True:
                print("\n" + "═" * 33)
                print(" ATBASH CIPHER ".center(30, "-"))
                print("═" * 33)
                print("  [1]  Encrypt/Decrypt 🔄")
                print("  [2]  About ℹ️")
                print("  [3]  Back to Main Menu 🔙")
                print("═" * 33)

                atbash_choice = check_int("👉 Choose an option [1-3]: ", 1, 3)

                if atbash_choice == 1:
                    print("\nRunning Atbash algorithm...")
                    text = get_input_atbash()
                    result_message = atbash_cipher(text)
                    print(f"\n Atbash message: {result_message}")

                elif atbash_choice == 2:
                    show_atbash_about()

                elif atbash_choice == 3:
                    break

        elif choice == 3:
            while True:
                print("\n" + "═" * 33)
                print(" VIGENÈRE CIPHER ".center(30, "-"))
                print("═" * 33)
                print("  [1]  Encrypt 🔒")
                print("  [2]  Decrypt 🔓")
                print("  [3]  About ℹ️")
                print("  [4]  Back to Main Menu 🔙")
                print("═" * 33)

                vigenere_choice = check_int("👉 Choose an option [1-4]: ", 1, 4)

                if vigenere_choice == 1:
                    print("\n[🔒] Running Vigenère Encrypt...")
                    text, key = get_input_vigenere()
                    encrypted_message = vigenere_cipher(text, key, decrypt=False)
                    print("\nEncrypted message:")
                    print(encrypted_message)

                elif vigenere_choice == 2:
                    print("\n[🔓] Running Vigenère Decrypt...")
                    text, key = get_input_vigenere()
                    decrypted_message = vigenere_cipher(text, key, decrypt=True)
                    print("\nDecrypted message:")
                    print(decrypted_message)

                elif vigenere_choice == 3:
                    show_vigenere_about()

                elif vigenere_choice == 4:
                    break

        elif choice == 4:
            print("\n👋 Exiting Cipher Tool. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
