    distinctChars := map[rune]int{}
    for _, char := range strings.ToLower(str) {
        distinctChars[char]++
    }
    return len(distinctChars)
}

func main() {
    fmt.Println(CountDistinctCharacters("xyzXYZ"))  // Output: 3
    fmt.Println(CountDistinctCharacters("Jerry"))  // Output: 4
}
```

**Python Solution:**

```python
def CountDistinctCharacters(str):
    str = str.lower()
    distinctChars = set(str)
    return len(distinctChars)

print(CountDistinctCharacters('xyzXYZ'))  # Output: 3
print(CountDistinctCharacters('Jerry'))  # Output: 4
```

In both solutions, we first convert the string to lowercase (this will make the counts case insensitive). Then we use a data structure (map in case of Go, set in case of Python) to store the distinct characters and their counts. Finally, we return the size of the data structure which gives us the count of distinct characters.

In Python, we use `set()` to get the distinct characters because it inherently avoids duplicates. In Go, we use a `map` where the keys are the characters and the values are the counts. We increment the count for each character as we encounter it.

Both solutions have a time complexity of O(n) where n is the length of the string. The space complexity is also O(n) where n is the number of distinct characters in the string.

In Go, the map is a reference type and it's not possible to create a map of uninitialized size. The `make()` function can be used to initialize a map, but it's not necessary to do this in this case because using `map[rune]int{}` initializes the map to an empty state.

In Python, we don't need to initialize a set because it is initialized to an empty state automatically.

Both solutions are correct and work as expected.






























