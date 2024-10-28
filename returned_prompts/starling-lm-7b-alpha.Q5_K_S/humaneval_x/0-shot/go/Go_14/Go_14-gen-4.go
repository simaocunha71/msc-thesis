
```go
package main

import (
	"fmt"
)

func AllPrefixes(str string) []string {
	res := []string{}
	for i := 0; i < len(str); i++ {
		res = append(res, str[:i+1])
	}
	return res
}

func main() {
	fmt.Println(AllPrefixes("abc"))
}
```

In this implementation, we use a for loop to iterate through each index of the string. We then use slicing to create a substring of the original string starting from the index and ending at the index plus one. We append each of these substrings to the `res` slice, which is initialized as an empty slice.

Finally, we return the `res` slice, which contains all the prefixes of the input string in order from shortest to longest.

For example, when we call `AllPrefixes("abc")`, the function will return `["a", "ab", "abc"]`, which are all the prefixes of the input string in the desired order.

This implementation has a time complexity of O(n), where n is the length of the input string, since we need to iterate through each index of the string once.

The space complexity is also O(n) in the worst case, as we need to store all the prefixes in the `res` slice. However, in practice, the space complexity will be O(1) for most inputs, since the length of the `res` slice will be at most equal to the length of the input string.

Overall, this implementation provides a simple and efficient solution to the problem of finding all the prefixes of a given string in order from shortest to longest.

// Return list of all prefixes from shortest to longest of the input string
// >>> AllPrefixes('abc')
// ['a', 'ab', 'abc']
func AllPrefixes(str string) []string {
    res := []string{}
    for i := 0; i < len(str); i++ {
        res = append(res, str[:i+1])
    }
    return res
}

In this implementation, we use a for loop to iterate through each index of the string. We then