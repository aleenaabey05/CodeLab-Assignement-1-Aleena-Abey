"""Exercise 08 - Simple Search

Search a list of names for a target string. By default the target is 'Sam',
but the user may enter a different search term. The search is case-insensitive.
"""

NAMES = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]


def find_name(target: str) -> int:
    """Return the index of the first match (case-insensitive), or -1 if not found."""
    t = target.strip().lower()
    for i, name in enumerate(NAMES):
        if name.lower() == t:
            return i
    return -1


def main() -> None:
    prompt = f"Enter name to search (default: Sam): "
    target = input(prompt).strip()
    if not target:
        target = "Sam"

    idx = find_name(target)
    if idx >= 0:
        print(f"Found '{NAMES[idx]}' at index {idx}.")
    else:
        print(f"'{target}' was not found in the list.")


if __name__ == "__main__":
    main()
