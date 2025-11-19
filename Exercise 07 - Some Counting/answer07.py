"""Exercise 07 - Some Counting

Prints sequences according to the exercise instructions.
"""

def main() -> None:
    print("1) Count up from 0 to 50:")
    for i in range(0, 51):
        print(i)

    print("\n2) Count down from 50 to 0:")
    for i in range(50, -1, -1):
        print(i)

    print("\n3) Count up from 30 to 50:")
    for i in range(30, 51):
        print(i)

    print("\n4) Count down from 50 to 10 in steps of 2:")
    for i in range(50, 9, -2):
        print(i)

    print("\n5) Count up from 100 to 200 in steps of 5:")
    for i in range(100, 201, 5):
        print(i)


if __name__ == "__main__":
    main()
