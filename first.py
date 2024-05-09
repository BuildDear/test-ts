from collections import defaultdict


def group_anagrams(strs):
    anagram_map = defaultdict(list)

    # Grouping the strings by sorted tuple of characters
    for s in strs:
        key = tuple(sorted(s))
        anagram_map[key].append(s)

    return list(anagram_map.values())


# Basic Functionality Tests
print("Test 1:", group_anagrams(["a", "b", "a"]))  # Expect: [['a', 'a'], ['b']]
print("Test 2:", group_anagrams(["ab", "ba", "abc", "bac"]))  # Expect: [['ab', 'ba'], ['abc', 'bac']]

# Intermediate Complexity Tests
print("Test 3:", group_anagrams(["dog", "god", "odg", "abc"]))  # Expect: [['dog', 'god', 'odg'], ['abc']]
print("Test 4:",
      group_anagrams(["hello", "marik", "world", "kirma"]))  # Expect: [['hello', 'olleh'], ['world', 'dlrow']]

# Advanced Complexity Tests
print("Test 5:", group_anagrams(["a" * 1000, "a" * 1000]))  # Large strings of same letters
print("Test 6:", group_anagrams(["x", "y", "z"]))  # Non-anagrams
print("Test 7:", group_anagrams(["eat", "tea", "ate", "eta", "aet"]))  # All anagrams
