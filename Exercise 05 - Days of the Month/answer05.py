"""Exercise 5: Days of the Month

Asks the user for a month number (1-12) and prints the number of days.
For February (2) the script asks whether it's a leap year and adjusts days.
"""

MONTH_DAYS = {
    1: 31,
    2: 28,  
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

MONTH_NAMES = {1: "January",2: "February",3: "March",4: "April",
5: "May",6: "June",7: "July",8: "August",9: "September",10: 
"October",11: "November",12: "December",}


def is_yes(text: str) -> bool:
    return text.strip().lower() in ("y", "yes", "true", "1")


def main() -> None:
    raw = input("Enter month number (1-12): ").strip()
    if not raw.isdigit():
        print("Invalid input: please enter a number between 1 and 12.")
        return

    month = int(raw)
    if month < 1 or month > 12:
        print("Invalid month: please enter a number between 1 and 12.")
        return

    days = MONTH_DAYS[month]
    month_name = MONTH_NAMES.get(month, f"Month {month}")

    if month == 2:
        leap = input("Is the year a leap year? (y/n): ").strip()
        if is_yes(leap):
            days = 29

    print(f"{month_name} ({month}) has {days} days.")


if __name__ == "__main__":
    main()
