# ============================================
# PALINDROME
# A string or number is a Palindrome if it reads
# the same forward and backward.
# Example: "racecar", 121
# ============================================

def is_palindrome_string(text):
    """Check if a string is a palindrome (ignores spaces and case)."""
    cleaned = ""
    for ch in text:
        if ch.isalnum():
            cleaned += ch.lower()

    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_number(number):
    """Check if a number is a palindrome without converting to string."""
    if number < 0:
        return False

    original = number
    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10

    return original == reversed_num


def longest_palindrome_substring(s):
    """Find the longest palindromic substring using expand-around-center."""
    if not s:
        return ""

    start = 0
    max_len = 1

    def expand(left, right):
        nonlocal start, max_len
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start = left
            left -= 1
            right += 1

    for i in range(len(s)):
        expand(i, i)       # Odd length
        expand(i, i + 1)   # Even length

    return s[start:start + max_len]


# ---- String Palindrome Check ----
strings = ["racecar", "hello", "A man a plan a canal Panama", "No lemon no melon"]
print("String Palindrome Check:")
print("-" * 40)
for s in strings:
    result = "✅ Palindrome" if is_palindrome_string(s) else "❌ Not Palindrome"
    print(f'"{s}" --> {result}')

# ---- Number Palindrome Check ----
numbers = [121, 123, 1221, 12321, -121]
print("\nNumber Palindrome Check:")
print("-" * 40)
for n in numbers:
    result = "✅ Palindrome" if is_palindrome_number(n) else "❌ Not Palindrome"
    print(f"{n} --> {result}")

# ---- Longest Palindromic Substring ----
test = "babad"
print(f'\nLongest Palindromic Substring in "{test}": "{longest_palindrome_substring(test)}"')
