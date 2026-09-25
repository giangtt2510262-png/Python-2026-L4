import math
import math

# 1. Circle Area
def task1():
    r = float(input("Enter circle radius? "))
    print(f"Circle area = {math.pi * r * r:.1f}")

# 2. Celsius to Fahrenheit
def task2():
    c = float(input("Enter the temperature in Celsius? "))
    print(f"{int(c)} (C) = {(c * 9/5) + 32:.1f} (F)")

# 3. Prime Check
def task3():
    n = int(input("Enter a number? "))
    is_p = n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))
    print(f"{n} is {'a prime' if is_p else 'a NOT prime'} number")

# 4. Perfect Check
def task4():
    n = int(input("Enter a number? "))
    is_pf = n > 0 and sum(i for i in range(1, n) if n % i == 0) == n
    print(f"{n} is {'a perfect' if is_pf else 'a NOT perfect'} number")

# 5. Search Color
def task5():
    colors = ["Red", "Blue", "Yellow", "Black", "White"]
    c = input("What is your favorite color? ")
    print(f"Your color is at index {colors.index(c)} in my list" if c in colors else "Sorry, I could not find your color")

# 6. Range Sequences
def task6():
    print("range1:", list(range(0, 7)))
    print("range2:", list(range(1, 11, 3)))
    print("range3:", list(range(5, 0, -1)))
    print("range4:", list(range(6, -3, -2)))

# 7. Remove Dollar Sign
def remove_dollar_sign(s):
    return s.replace("$", "")

# 8. Extract Even Items
def extract_even(l):
    return [x for x in l if x % 2 == 0]

# 9. Factorial
def factorial(n):
    return math.factorial(n) if n >= 0 else None

# 10. Divisors
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# 11. Distance
def compute_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# 12. Pattern m x n
def print_pattern(m, n):
    for _ in range(m):
        print("*" * n)