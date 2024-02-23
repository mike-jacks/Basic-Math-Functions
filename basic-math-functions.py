def add(x: float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x * y

def square(x: float) -> float:
    return multiply(x, x)

def add_squares(x: float, y: float) -> float:
    return add(square(x), square(y))

def main():
    x = 5
    y = 7 
    print(f"add: add({x},{y}) = {add(x,y)}")
    print(f"multiply: multiply({x},{y}) = {multiply(x,y)}")
    print(f"square: square({x}) = {square(x)}")
    print(f"square: square({y}) = {square(y)}")
    print(f"add_squares: add_squares({x},{y}) = {add_squares(x,y)}")

if __name__ == "__main__":
    main()
