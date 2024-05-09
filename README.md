# TASK 1: Group Anagrams Function

## Code Overview
The `group_anagrams` function uses Python's `collections.defaultdict` to group strings that are anagrams of each other into lists, based on their sorted character tuples as keys.

## Test Results
- **Test 1**: Input `["a", "b", "a"]` outputs `[['a', 'a'], ['b']]`.
- **Test 2**: Input `["ab", "ba", "abc", "bac"]` outputs `[['ab', 'ba'], ['abc', 'bac']]`.
- **Test 3**: Input `["dog", "god", "odg", "abc"]` outputs `[['dog', 'god', 'odg'], ['abc']]`.
- **Test 4**: Complex word test, successfully groups `["hello", "olleh"]` and `["world", "dlrow"]`.
- **Test 5**: Handles large identical strings efficiently.
- **Test 6**: Correctly identifies non-anagrams.
- **Test 7**: Efficiently groups multiple permutations of the same letters.

## Complexity Analysis
- **Time Complexity**: ( O(n * k log(k)) ) 
- **Space Complexity**: ( O(n * k) )
- Where ( n ) is the number of strings and ( k ) is their maximum length.

## Conclusion
The function is efficient and robust, suitable for varying input complexities. It demonstrates effectiveness with sorted keys but may require optimization for very large datasets.

# TASK 2: Performance Measurement of Anagram Grouping

## Code Overview
The script measures the execution time of the `group_anagrams` function with increasing numbers of generated anagram strings. It uses `matplotlib` to plot these times against the number of strings.

## Performance Evaluation
- **Data Sizes**: Tests conducted for sizes ranging from 100 to 50,000 strings.
- **String Length**: Each string has a length of 3 characters.
- **Execution Time**: Observed times increase linearly with the number of strings, indicating predictable scalability.

## Test Output
The graph visualizes execution times, showing a clear trend of increasing time with larger datasets, which assists in assessing the function's performance under load.

## Conclusion
The script is effectively used to benchmark the `group_anagrams` function. It illustrates the function's behavior with increasing input sizes and provides a visual understanding of scalability. Optimization might be needed for high-performance requirements in larger datasets.
