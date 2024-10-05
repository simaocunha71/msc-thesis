Here is the solution:

```go
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
```


Explanation:
The function `FilterBySubstring` takes two parameters: a list of strings (`stringList`) and a substring (`substring`). It initializes an empty slice (`filteredList`) to store the filtered strings. 

Then, it iterates over the input list (`stringList`) using a range loop. For each string in the list, it checks if the substring is present in the string using the `strings.Contains` function. If the substring is found, the string is appended to the `filteredList`.

Finally, the function returns the `filteredList`, which contains only the strings that contain the given substring. 