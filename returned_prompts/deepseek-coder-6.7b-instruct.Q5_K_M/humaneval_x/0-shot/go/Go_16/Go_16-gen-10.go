    // 1. Convert string to lowercase
    lowerStr := strings.ToLower(str)

    // 2. Create a map to store distinct characters
    distinctChars := make(map[rune]bool)

    // 3. Iterate over the string
    for _, char := range lowerStr {
        // 4. Check if character is already in the map
        _, ok := distinctChars[char]

        // 5. If it is not, add it to the map
        if !ok {
            distinctChars[char] = true
        }
    }

    // 6. Return the length of the map
    return len(distinctChars)
}
```

### Python Solution:
```python
# Given a string, find out how many distinct characters (regardless of case) does it consist of
# >>> count_distinct_characters('xyzXYZ')
# 3
# >>> count_distinct_characters('Jerry')
# 4
def count_distinct_characters(s):
    # 1. Convert string to lowercase
    lower_s = s.lower()

    # 2. Create a set to store distinct characters
    distinct_chars = set()

    # 3. Iterate over the string
    for char in lower_s:
        # 4. Add character to the set
        distinct_chars.add(char)

    # 5. Return the length of the set
    return len(distinct_chars)
```

### JavaScript Solution:
```javascript
// Given a string, find out how many distinct characters (regardless of case) does it consist of
// console.log(countDistinctCharacters('xyzXYZ')); // 3
// console.log(countDistinctCharacters('Jerry')); // 4
function countDistinctCharacters(str) {
    // 1. Convert string to lowercase
    let lowerStr = str.toLowerCase();

    // 2. Create a set to store distinct characters
    let distinctChars = new Set();

    // 3. Iterate over the string
    for (let char of