import sys


def main() -> None:
    if len(sys.argv) < 4:
        print("Usage: python profile.py ROAA 22 Palistine")
        sys.exit(1)

    name: str = sys.argv[1]
    age: int = int(sys.argv[2])
    country: str = sys.argv[3]

    print("-" * 22)
    print(f"Name    : {name}")
    print(f"Age     : {age}")
    print(f"Country : {country}")
    print("-" * 22)


if __name__ == "__main__":
    main()
