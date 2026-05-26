# ============================================
# ANAGRAM
# Two strings are Anagrams if they contain the
# same characters in any order.
# Example: "listen" and "silent" are anagrams.
# ============================================

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Must be the same length
    if len(str1) != len(str2):
        return False

    # Count character frequency without built-in Counter
    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False

    # All counts should be zero
    for count in char_count.values():
        if count != 0:
            return False

    return True


def find_anagram_groups(words):
    """Group a list of words into anagram families."""
    groups = {}
    for word in words:
        key = ''.join(sorted(word.lower()))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return [group for group in groups.values() if len(group) > 1]


# ---- Check Two Strings ----
pairs = [
    ("listen", "silent"),
    ("hello",  "world"),
    ("Astronomer", "Moon starer"),
    ("Python", "Typhon"),
]

print("Anagram Check:")
print("-" * 35)
for a, b in pairs:
    result = "✅ Anagram" if is_anagram(a, b) else "❌ Not Anagram"
    print(f'"{a}" & "{b}" --> {result}')

# ---- Group Anagrams ----
word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("\nAnagram Groups from:", word_list)
groups = find_anagram_groups(word_list)
for g in groups:
    print(" ", g)
