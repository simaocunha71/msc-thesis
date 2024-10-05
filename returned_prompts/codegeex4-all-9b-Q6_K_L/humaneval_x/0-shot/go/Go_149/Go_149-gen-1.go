To solve this problem, you can follow these steps:

1. Iterate through the list `lst` and delete the strings that have odd lengths.
2. Sort the resulting list alphabetically.
3. Return the sorted list.

Here is the Go code that implements this algorithm:

```go
import (
    "sort"
)

func SortedListSum(lst []string) []string {
    // Step 1: Delete strings with odd lengths
    for i := 0; i < len(lst); i++ {
        if len(lst[i])%2 != 0 {
            lst = append(lst[:i], lst[i+1:]...)
            i--
        }
    }

    // Step 2: Sort the list alphabetically
    sort.Strings(lst)

    // Step 3: Return the sorted list
    return lst
}
```

Now you can test the function using the provided test cases:

```go
func main() {
    // Test cases
    assertEqual(SortedListSum([]string{"aa", "a", "aaa"}), []string{"aa"})
    assertEqual(SortedListSum([]string{"ab", "a", "aaa", "cd"}), []string{"ab", "cd"})
}

func assertEqual(a, b []string) {
    if len(a) != len(b) {
        fmt.Printf("Assertion failed: Lengths are not equal (%d != %d)\n", len(a), len(b))
        return
    }

    for i := range a {
        if a[i] != b[i] {
            fmt.Printf("Assertion failed: Elements are not equal at index %d (%s != %s)\n", i, a[i], b[i])
            return
        }
    }

    fmt.Println("Assertion passed")
}
```

This code should output:

```
Assertion passed
Assertion passed
```