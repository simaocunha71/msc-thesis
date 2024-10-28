
To solve this problem we need to iterate through the string and take a slice of the string from the start index to the current index. We then append the slice to our result list and increment the index.

```go
package main

import "fmt"

func AllPrefixes(str string) []string {
	var result []string
	for i := 0; i < len(str); i++ {
		result = append(result, str[:i+1])
	}
	return result
}

func main() {
	str := "abc"
	fmt.Println(AllPrefixes(str)) // ['a', 'ab', 'abc']
}
```

In this solution we start by creating an empty result slice. We then iterate through the input string starting from the first character and ending at the current index. For each character we take a slice from the start of the string to the current index (inclusive) and append this slice to our result slice. We then increment the index and continue the process until we have gone through the entire input string. Finally we return the result slice containing all of the prefixes of the input string.

This solution has a time complexity of O(n) where n is the length of the input string. This is because we only iterate through the input string once. The space complexity is also O(n) because we store all of the prefixes in our result slice. 

Note: In Go, slicing a string returns a new string that shares the underlying data with the original string. This means that slicing a string is a cheap operation and does not require copying the entire string. 

In terms of performance, this solution should be quite efficient for most cases. However, if you are working with very long strings or large amounts of data, you may want to consider using a more efficient data structure or algorithm.

I hope this helps! Let me know if you have any more questions. 

Here is the code and the output:

```go
package main

import "fmt"

func AllPrefixes(str string) []string {
	var result []string
	for i := 0; i < len(str); i++ {
		result = append(result, str[:i+1])
	}
	return result
