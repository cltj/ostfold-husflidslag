def hello(name: str) -> str:
    """Return a greeting"""
    return f"Hello, {name}!"

def main() -> None:
    print(hello("World"))

if __name__ == "__main__":
    main()