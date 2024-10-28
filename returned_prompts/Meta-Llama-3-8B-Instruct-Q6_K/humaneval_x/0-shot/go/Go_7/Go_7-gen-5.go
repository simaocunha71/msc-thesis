Here is a simple and efficient solution using the `strings.Contains` function from the `strings` package:

```go
package main

import (
    "strings"
)

// Filter an input list of strings only for ones that contain given substring
func FilterBySubstring(stringList []string, substring string) []string {
    var result []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            result = append(result, str)
        }
    }
    return result
}

func main() {
    strList := []string{"abc", "bacd", "cde", "array"}
    subStr := "a"
    result := FilterBySubstring(strList, subStr)
    for _, str := range result {
        println(str)
    }
}
```

This program defines a function `FilterBySubstring` that takes a list of strings and a substring as input, and returns a new list containing only the strings from the original list that contain the given substring. It uses a loop to iterate over the input list, and for each string, it checks if the substring is contained within the string using the `strings.Contains` function. If it is, the string is added to the result list. The function returns the result list.

In the `main` function, we demonstrate how to use this function by creating a list of strings, a substring, and then calling `FilterBySubstring` with these inputs. The function returns a new list containing the strings that contain the given substring, which we then print to the console. The output will be:

```
abc
bacd
array
```


This is the expected output, as these are the strings from the original list that contain the substring "a". The other strings do not contain "a" and are therefore not included in the result list.