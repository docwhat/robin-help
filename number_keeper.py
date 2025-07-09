#!/usr/bin/env python3


class NumberKeeper:
    def __init__(self, initial_number: int = None):
        "Optionally, sets kept number on creation."
        self.number = initial_number

    def set(self, new_number: int) -> None:
        "Set the kept number, overwriting the previous value."
        self.number = new_number

    def get(self) -> int:
        "Returns the kept number."
        return self.number

    def __str__(self) -> str:
        return f"Kept Value: {repr(self.number)}"


if __name__ == "__main__":
    z = NumberKeeper()
    print(f"Ready!")
