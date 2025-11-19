"""Exercise 10: Is it even?

Prompts the user for a number in main(), passes it to a function
that determines if it is even or odd, and prints the returned message.
"""

def even_or_odd(number: int) -> str:
    """Return a message indicating whether `number` is even or odd."""
    if number % 2 == 0:
        return f"{number} is even"
    return f"{number} is odd"


def main() -> None:
    raw = input("Enter a number: ").strip()
    try:
        n = int(raw)
    except ValueError:
        print("Invalid input: please enter an integer.")
        return

    msg = even_or_odd(n)
    print(msg)


if __name__ == "__main__":
    main()
