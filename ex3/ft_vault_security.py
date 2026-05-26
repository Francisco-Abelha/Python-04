def secure_archive(
    fname: str, action: int = 0, content: str = ""
) -> tuple[bool, str]:
    try:
        if action == 0:
            with open(fname, "r") as file:
                content_read: str = file.read()
                return (True, content_read)
        elif action == 1:
            with open(fname, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action command")
    except (FileNotFoundError, PermissionError) as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    test1 = secure_archive("/not/existing/file", 0)
    print(f"{test1}\n")
    print("Using 'secure_archive' to read from an inaccessible file:")
    test2 = secure_archive("forbiden.txt", 0)
    print(f"{test2}\n")
    print("Using 'secure_archive' to read from a regular file:")
    test3 = secure_archive("ancient_fragment.txt", 0)
    print(f"{test3}\n")
    print("Using 'secure_archive' to write previous content to a new file:")
    test4 = secure_archive("new_ancient_fragment.txt", 1, test3[1])
    print(f"{test4}\n")


if __name__ == "__main__":
    main()
