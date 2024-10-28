Here's the solution. First, it creates a map to convert words to numbers. Then it splits the input string into words, converts each word to its corresponding number, and stores each number with its corresponding word in a multimap. Finally, it iterates over the multimap and constructs the result string.

The time complexity of this solution is O(n log n) because of the sorting operation.

The space complexity is O(n) because we store the words and their corresponding numbers in a map and a multimap.

Note: This solution assumes that the input string is well-formed and does not contain any invalid words.

The solution is written in C++.

If you have any questions, feel free to ask.

