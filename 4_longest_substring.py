# ============================================
# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# Find the length and the actual substring of the
# longest window with all unique characters.
# Example: "abcabcbb" --> "abc" (length 3)
# ============================================

def longest_unique_substring(s):
    """
    Sliding Window approach — O(n) time, O(k) space
    where k is the size of the character set.
    """
    char_index = {}   # stores last seen index of each character
    start = 0
    max_len = 0
    max_start = 0

    for end in range(len(s)):
        char = s[end]

        # If char was seen and is inside the current window, shrink from left
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = end

        window_len = end - start + 1
        if window_len > max_len:
            max_len = window_len
            max_start = start

    longest = s[max_start: max_start + max_len]
    return max_len, longest


def all_unique_substrings(s):
    """Return all unique-character substrings (brute force for understanding)."""
    result = []
    n = len(s)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            result.append(s[i:j+1])
    return result


# ---- Main Tests ----
test_cases = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "dvdf",
    "abcdefg",
    "",
    "au",
]

print("Longest Substring Without Repeating Characters")
print("=" * 50)
for s in test_cases:
    length, substring = longest_unique_substring(s)
    print(f'Input : "{s}"')
    print(f'Result: Length = {length},  Substring = "{substring}"')
    print("-" * 50)
