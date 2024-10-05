
}

I'm trying to solve this problem in Golang. I'm not sure how to start this problem as I'm not sure what to look for in the question. 

A: This problem can be solved by following these steps:
1. Create a new slice to store the strings with even length.
2. Iterate over the input list, and add the string to the new slice if its length is even.
3. Sort the new slice by length of each string, and then alphabetically.
4. Return the sorted slice.

Here is the code:
```go
package main

import (
    "fmt"
    "sort"
)

type ByLengthAndAlphabet []string

func (s ByLengthAndAlphabet) Len() int {
    return len(s)
}
func (s ByLengthAndAlphabet) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
}
func (s ByLengthAndAlphabet) Less(i, j int) bool {
    if len(s[i]) != len(s[j]) {
        return len(s[i]) < len(s[j])
    }
    return s[i] < s[j]
}

func SortedListSum(lst []string) []string {
    var evenStrings []string
    for _, str := range lst {
        if len(str)%2 == 0 {
            evenStrings = append(evenStrings, str)
        }
    }
    sort.Sort(ByLengthAndAlphabet(evenStrings))
    return evenStrings
}

func main() {
    fmt.Println(SortedListSum([]string{"ab", "a", "aaa", "cd"}))
}
```
This code will output: `[ab cd]`.

In the code, we have created a new type `ByLengthAndAlphabet` that implements the `sort.Interface`. The `Less` method returns true if the string at index i is shorter or has a smaller alphabetical order than the string at index j, or if the lengths are the same but the string at index i comes before