"""Exercise 6: Brute Force Attack

Basic behaviour:
- The correct password is defined as 12345.
- The program repeatedly prompts for a password until the correct one is entered.
- Prints an appropriate message when access is granted.
"""

CORRECT_PASSWORD = "12345"

def main() -> None:
    prompt = "Enter password: "
    user = input(prompt)
    while user != CORRECT_PASSWORD:
        print("Incorrect password. Try again.")
        user = input(prompt)

    print("Access granted. Correct password entered.")


if __name__ == "__main__":
    main()
