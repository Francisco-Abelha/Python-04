import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        try:
            fname: str = sys.argv[1]
            print(f"Accessing file '{fname}'")
            f: typing.IO[str] = open(fname, 'r')
            print("---\n")
            print(f.read())
            f.close()
            print("\n---")
            print(f"File '{fname}' closed.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{fname}': {e}")


if __name__ == "__main__":
    main()
