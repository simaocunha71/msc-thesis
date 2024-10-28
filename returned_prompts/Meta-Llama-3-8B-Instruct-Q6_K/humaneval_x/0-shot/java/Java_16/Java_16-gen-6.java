```java
public int countDistinctCharacters(String string) {
    String s = string.toLowerCase();
    Set<Character> set = new HashSet<>();
    for (char c : s.toCharArray()) {
        set.add(c);
    }
    return set.size();
}
```
Explanation:
This solution converts the input string to lowercase using the `toLowerCase()` method to ensure the comparison is case-insensitive.
It then uses a `HashSet` to store the distinct characters in the string. `HashSet` automatically removes duplicates, so we don't need to worry about counting the same character multiple times.
Finally, it returns the size of the `HashSet`, which represents the number of distinct characters in the string.
For example, if the input is "xyzXYZ", the output will be 3, because there are 3 distinct characters: 'x', 'y', and 'z'. If the input is "Jerry", the output will be 4, because there are 4 distinct characters: 'j', 'e', 'r', and 'y'. 

This solution has a time complexity of O(n), where n is the length of the input string, because it needs to iterate over each character in the string. The space complexity is also O(n), because in the worst case (when all characters are distinct), the `HashSet` will store n characters. 

This solution is efficient and easy to understand, making it a good choice for this problem. 