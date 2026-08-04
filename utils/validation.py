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
