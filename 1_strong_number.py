# ============================================
# STRONG NUMBER
# A number is a Strong Number if the sum of
# factorials of its digits equals the number itself.
# Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
# ============================================

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_strong_number(number):
    temp = number
    total = 0

    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10

    return total == number

def find_strong_numbers(start, end):
    strong_numbers = []
    for num in range(start, end + 1):
        if is_strong_number(num):
            strong_numbers.append(num)
    return strong_numbers


# ---- Single Number Check ----
num = 145
if is_strong_number(num):
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is NOT a Strong Number")

# ---- Find all Strong Numbers in a Range ----
print("\nStrong Numbers between 1 and 100000:")
results = find_strong_numbers(1, 100000)
print(results)
