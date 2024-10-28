```go
func SortedListSum(lst []string) []string {
    sort.SliceStable(lst, func(i, j int) bool {
        if len(lst[i]) == len(lst[j]) {
            return lst[i] < lst[j]
        }
        return len(lst[i]) < len(lst[j])
    })
    return filterOddLength(lst)
}

func filterOddLength(lst []string) []string {
    result := make([]string, 0)
    for _, str := range lst {
        if len(str)%2 == 0 {
            result = append(result, str)
        }
    }
    return result
}
```

Explanation:
The problem requires us to create a function that takes a list of strings as input, removes the strings with odd lengths, and returns the resulting list in a sorted order. The sorting should be done based on the length of each word first, and then alphabetically if two words have the same length.

To solve this problem, we can use the built-in `sort` package in Go. We can use the `SliceStable` function from this package to sort the list of strings. The `SliceStable` function takes a function as an argument, which is used to compare two elements in the list and determine their order.

In our case, we can use a lambda function to compare two elements. The lambda function checks if the lengths of the two strings are equal. If they are equal, it compares the strings alphabetically. If they are not equal, it compares the lengths. This ensures that the list is sorted by length first, and then alphabetically if two words have the same length.

After sorting the list, we can use another function `filterOddLength` to remove the strings with odd lengths from the list. This function iterates over the list, checks the length of each string, and appends the strings with even lengths to a new list.

Finally, we return the resulting list.

The unit tests provided in the problem ensure that the function works correctly. For example, the test `assert list_sort(["aa", "a", "aaa"]) => ["aa"]` checks that the function returns a list with only the strings with even lengths, and the test `assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]` checks that the function sorts the list by length first, and then alphabetically if two words have the same length.