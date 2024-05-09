import random
import string
import time
from collections import defaultdict

import matplotlib.pyplot as plt


# From the 1st task
def group_anagrams(strs):
    anagram_map = defaultdict(list)

    # Grouping the strings by sorted tuple of characters
    for s in strs:
        key = tuple(sorted(s))
        anagram_map[key].append(s)

    return list(anagram_map.values())


# Generate a random string of the given length
def generate_anagram_strs(size: int, length: int) -> [str]:
    base_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    anagrams = []
    base_list = list(base_string)

    for _ in range(size):
        random.shuffle(base_list)
        anagrams.append(''.join(base_list))

    return anagrams


# Function to measure and plot performance
def measure_performance():
    sizes = [100, 200, 500, 1000, 2000, 5000, 10000, 50000]
    lengths = 3
    times = []

    # Test the performance for different sizes
    for size in sizes:
        strs = generate_anagram_strs(size, lengths)

        start_time = time.time()
        group_anagrams(strs)
        end_time = time.time()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)

    # Plotting the results
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, times, marker='o')
    plt.title('Performance of group_anagrams Function')
    plt.xlabel('Number of Anagrams')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()


measure_performance()
