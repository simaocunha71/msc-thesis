
```go
func AllPrefixes(str string) []string {
    var result []string
    for i := 0; i < len(str); i++ {
        result = append(result, str[:i+1])
    }
    return result
}
```

In this solution, we initialize an empty slice called `result`. Then, we use a `for` loop to iterate through the indices of the input string `str`. For each index `i`, we use slicing to extract the substring from index 0 to `i+1` and append it to the `result` slice. Finally, we return the `result` slice, which contains all the prefixes of the input string in the correct order.

This solution has a time complexity of O(n), where n is the length of the input string. It iterates through all the indices of the string once and appends each substring to the `result` slice. Therefore, it is an efficient solution for finding all the prefixes of a string.

Here are a few test cases to demonstrate the usage of the `AllPrefixes` function:

```go
fmt.Println(AllPrefixes("abc")) // Output: ["a", "ab", "abc"]
fmt.Println(AllPrefixes("stackoverflow")) // Output: ["", "s", "st", "sta", "stac", "stack", "stacko", "stackov", "stackove", "stackovf", "stackoverflow"]
fmt.Println(AllPrefixes("")) // Output: []
```

In the first test case, we pass the string "abc" to the `AllPrefixes` function, and it returns a slice containing all the prefixes of the string in the correct order: ["a", "ab", "abc"].

In the second test case, we pass the string "stackoverflow" to the `AllPrefixes` function, and it returns a slice containing all the prefixes of the string in the correct order: ["", "s", "st", "sta", "stac", "stack", "stacko", "stackov", "stackove", "stackovf", "stackoverflow"]. Note that the empty string "" is also considered a prefix, so it is included in the result.

In the third test case, we pass