Here is the solution:

```go
package main

import (
    "strings"
)

// Filter an input list of strings only for ones that contain given substring
// >>> FilterBySubstring([], 'a')
// []
// >>> FilterBySubstring(['abc', 'bacd', 'cde', 'array'], 'a')
// ['abc', 'bacd', 'array']
func FilterBySubstring(stringList []string, substring string) []string {
    var filteredList []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            filteredList = append(filteredList, str)
        }
    }
    return filteredList
}

func main() {
    result := FilterBySubstring([]string{"abc", "bacd", "cde", "array"}, "a")
    for _, str := range result {
        println(str)
    }
}
```

In this code, we use the `strings.Contains` function to check if a string contains the given substring. If it does, we add it to our `filteredList`. The function returns this `filteredList`. In the `main` function, we test this function with a sample input. The output will be:

```
abc
bacd
array
```  which are the strings that contain the substring 'a'.  If you run the program with an empty input list, the output will be an empty list.  If you run the program with a non-existent substring, the output will be an empty list.  The function works as expected.  You can also test it with different inputs to see how it works.  It's a simple but useful function.  It's also worth noting that this function is case sensitive.  If you want it to be case insensitive, you can convert both the string and the substring to lower case or upper case before checking if the string contains the substring.  You can do this by using the `strings.ToLower` or `strings.ToUpper` function.  For example, you could use `strings.Contains(strings.ToLower(str), strings.ToLower(substring))`.  This way, the function will work the same way regardless of the case of the input strings.  This is a common requirement in many applications.  It's also worth noting that this function has a time complexity of O(n), where n is the number of strings in the input list.  This is because it has to iterate over all the strings in the list.  This is not a problem for small lists, but