# ============================================
# REMOVE DUPLICATES WITHOUT BUILT-IN FUNCTIONS
# No set(), no dict.fromkeys(), no Counter,
# no list comprehension tricks — pure logic only.
# ============================================

# ---- From a List (preserve order) ----
def remove_duplicates_list(lst):
    seen = []
    result = []
    for item in lst:
        found = False
        for s in seen:
            if s == item:
                found = True
                break
        if not found:
            seen.append(item)
            result.append(item)
    return result


# ---- From a String (preserve order) ----
def remove_duplicates_string(text):
    seen = []
    result = ""
    for ch in text:
        found = False
        for s in seen:
            if s == ch:
                found = True
                break
        if not found:
            seen.append(ch)
            result += ch
    return result


# ---- From a Sorted List (O(n) in-place approach) ----
def remove_duplicates_sorted(lst):
    if not lst:
        return []
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] != lst[i - 1]:
            result.append(lst[i])
    return result


# ---- From a String — keep only characters that appear once ----
def keep_unique_only(text):
    """Keep characters that appear exactly once."""
    # Count manually
    count = {}
    for ch in text:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    result = ""
    for ch in text:
        if count[ch] == 1:
            result += ch
    return result


# ---- Tests ----
print("Remove Duplicates from List:")
print("-" * 40)
lists = [
    [1, 2, 3, 2, 1, 4, 5, 4],
    ["apple", "banana", "apple", "cherry", "banana"],
    [10, 10, 10, 10],
]
for l in lists:
    print(f"Input : {l}")
    print(f"Output: {remove_duplicates_list(l)}")
    print()

print("Remove Duplicates from String:")
print("-" * 40)
strings = ["programming", "hello world", "aabbccdd"]
for s in strings:
    print(f'Input : "{s}"')
    print(f'Output: "{remove_duplicates_string(s)}"')
    print()

print("Remove Duplicates from Sorted List:")
print("-" * 40)
sorted_list = [1, 1, 2, 3, 3, 3, 4, 5, 5]
print(f"Input : {sorted_list}")
print(f"Output: {remove_duplicates_sorted(sorted_list)}")
print()

print("Keep Only Unique Characters (appear once):")
print("-" * 40)
word = "programming"
print(f'Input : "{word}"')
print(f'Output: "{keep_unique_only(word)}"')
