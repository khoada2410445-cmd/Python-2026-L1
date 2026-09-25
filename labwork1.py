import math

# Task 1: Circle Area
def task_1():
    radius = float(input("Enter circle radius? "))
    area = math.pi * radius * radius
    print(f"Circle area = {area:.1f}")

# Task 2: Celsius to Fahrenheit
def task_2():
    celsius = float(input("Enter the temperature in Celsius? "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{int(celsius)} (C) = {fahrenheit:.1f} (F)")

# Task 3: Check Prime Number
def task_3():
    num = int(input("Enter a number? "))
    if num < 2:
        print(f"{num} is a NOT prime number")
        return
    
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is a NOT prime number")

# Task 4: Check Perfect Number
def task_4():
    num = int(input("Enter a number? "))
    if num <= 0:
        print(f"{num} is a NOT perfect number")
        return

    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    
    if divisors_sum == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is a NOT perfect number")

# Task 5: Search Color in List
def task_5():
    colors = ["Blue", "Yellow", "Black", "Red", "White", "Pink"]
    fav_color = input("What is your favorite color? ").strip()
    
    found = False
    for index, color in enumerate(colors):
        if color.lower() == fav_color.lower():
            print(f"Your color is at index {index} in my list")
            found = True
            break
            
    if not found:
        print("Sorry, I could not find your color")

# Task 6: Print Sequences using range()
def task_6():
    range1 = list(range(0, 7))
    range2 = list(range(1, 11, 3))
    range3 = list(range(5, 0, -1))
    range4 = list(range(6, -3, -2))

    print("range1:", range1)
    print("range2:", range2)
    print("range3:", range3)
    print("range4:", range4)

# Task 7: Remove Dollar Sign
def remove_dollar_sign(s):
    return s.replace("$", "")

# Task 8: Extract Even Numbers
def extract_even(l):
    return [x for x in l if x % 2 == 0]

# Task 9: Factorial
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Task 10: Get Divisors
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Task 11: Distance Between Two Points
def compute_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Task 12: Print Pattern m x n
def print_pattern(m, n):
    for _ in range(m):
        print("*" * n)


if __name__ == "__main__":
    print("--- Testing Labwork 1 ---")
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    
    print("\nTest Task 7:", remove_dollar_sign("100$ USD"))
    print("Test Task 8:", extract_even([1, 4, 5, -1, 10]))
    print("Test Task 9:", factorial(5))
    print("Test Task 10:", get_divisors(12))
    print("Test Task 11:", compute_distance(0, 0, 3, 4))
    print("Test Task 12:")
    print_pattern(3, 5)