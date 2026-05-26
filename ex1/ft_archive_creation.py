import sys
import typing


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        try:
            fname: str = sys.argv[1]
            print(f"Accessing file '{fname}'")
            f: typing.IO[str] = open(fname, 'r')
            print("---\n")
            file_string: str = f.read()
            print(file_string)
            f.close()
            print("\n---")
            print(f"File '{fname}' closed.\n")
            try:
                print("Transform data:")
                print("---\n")
                splitted: list[str] = file_string.splitlines()
                splitted = [line + "#" for line in splitted]
                joined: str = "\n".join(splitted)
                print(joined)
                print("---")
                new_file = input("Enter new file name (or empty): ")
                if new_file == "":
                    print("Not saving data.")
                    return
                f2: typing.IO[str] = open(new_file, 'w')
                print(f"Saving data to '{new_file}'")
                f2.write(joined)
                f2.close()
                print(f"Data saved in file '{new_file}'")
            except PermissionError as e:
                print(f"Error opening file '{new_file}': {e}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{fname}': {e}")


if __name__ == "__main__":
    main()
