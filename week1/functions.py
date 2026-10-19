def greet(name: str, greeting:str = "Hello") -> str:
    return f"{greeting}, {name}!"

def total(*number: int) -> int:
    return sum(number)

def create_user(**fields) -> dict:
    return {id: 1, **fields}

print(greet("Alice"))
print(greet("Bob", greeting="Hi"))
print(total(1, 2, 3, 4, 5))
print(create_user(name="Alice", role="admin", email="alice@example.com"))

def apply(func, value):
    return func(value)

print(apply(str.upper, "hello"))
print(sorted(["bb", "a", "ccc"], key=len))
print(list(map(lambda x: x**2, [1, 2, 3])))