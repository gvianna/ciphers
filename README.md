# 🔐 Ciphers

A collection of **classical substitution ciphers** implemented in Python.

This project was developed as part of my **Python** studies during my degree in **Systems Analysis and Development**, focusing on algorithm implementation, code organization, and the application of programming concepts.

## ✨ Features

The project currently includes three encryption algorithms:

* **Caesar Cipher** — shifts letters of the alphabet
* **Atbash Cipher** — replaces each letter with its corresponding position in the reversed alphabet
* **Vigenère Cipher** — a polyalphabetic cipher based on a keyword

The program features an interactive menu that allows users to select an algorithm and perform **encryption and decryption** operations.

## 🔑 Implemented Ciphers

### Caesar Cipher

The Caesar cipher shifts each letter of the text by a specified number of positions in the alphabet.

For example, with a shift of `3`:

```text
A → D
B → E
C → F
```

Example:

```text
HELLO
```

with a shift of `3`:

```text
KHOOR
```

Decryption uses the inverse shift.

---

### Atbash Cipher

The Atbash cipher uses the reversed alphabet to perform the substitution:

```text
A ↔ Z
B ↔ Y
C ↔ X
```

Example:

```text
HELLO
```

results in:

```text
SVOOL
```

Since the transformation is symmetric, the same algorithm can be used for both encryption and decryption.

---

### Vigenère Cipher

The Vigenère cipher uses a **keyword** to determine different shifts throughout the text.

For example, using the key:

```text
KEY
```

each letter of the key determines the shift applied to the corresponding letter of the message.

Unlike the Caesar cipher, the shift is not necessarily the same throughout the entire text.

## 🛠️ Technologies

* **Python 3**
* Python Standard Library

The project does not depend on external libraries to perform the encryption algorithms.

## 📁 Project Structure

```text
ciphers/
│
├── algorithms/
│   └── ciphers.py
│
├── utils/
│   └── validation.py
│
├── main.py
├── README.md
└── .gitignore
```

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/SEU-USUARIO/ciphers.git
```

Navigate to the project directory:

```bash
cd ciphers
```

Run the program:

```bash
python main.py
```

The main menu allows you to choose the cipher and the desired operation.

## 🔎 Input Validation

The project includes validation functions to handle user-provided input.

The validated inputs include:

* Text used in messages
* Integer values
* Valid ranges for shifts
* Keys used by the Vigenère cipher

The validation logic is separated from the rest of the program to maintain better code organization.

## 🧠 Concepts Practiced

The development of this project provides practice with several fundamental Python concepts:

* Functions
* Modules and imports
* Lists and strings
* Loops
* Conditionals
* Character manipulation
* `ord()` and `chr()`
* Modulo operator `%`
* Data validation
* Organizing projects into multiple files
* Function reuse
* Separation of responsibilities

## ⚠️ Note

The ciphers implemented in this project are **historical cryptographic algorithms** and should not be used to protect real information.

Ciphers such as Caesar, Atbash, and Vigenère can be broken using relatively simple techniques and are primarily intended for **educational purposes**.

## 📜 License

This project was developed for educational and study purposes.
