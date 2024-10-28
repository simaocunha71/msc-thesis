You can use the strings.Count function to count the number of times a substring occurs in a string. This function takes two arguments: the string to search and the substring to count. It returns the number of times the substring is found in the string.

Here's the updated code:

```go
func HowManyTimes(str string, substring string) int {
	return strings.Count(str, substring)
}
```

This code will count the number of times the substring occurs in the original string, including overlapping cases.