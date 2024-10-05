```go
func SortedListSum(lst []string) []string {
    sort.SliceStable(lst, func(i, j int) bool {
        if len(lst[i]) == len(lst[j]) {
            return lst[i] < lst[j]
        }
        return len(lst[i]) < len(lst[j])
    })
    result := make([]string, 0)
    for _, str := range lst {
        if len(str)%2 == 0 {
            result = append(result, str)
        }
    }
    return result
}
```  



The function `SortedListSum` takes a list of strings as an input, removes the strings with odd lengths, and returns the resulted list in a sorted order. The list is always a list of strings and never an array of numbers, and it may contain duplicates. The order of the list is first sorted by the length of each word in ascending order, and then alphabetically if two words have the same length. The function returns a list of strings in the sorted order. 

First, we sort the list of strings using the `sort.SliceStable` function. The comparison function provided to `sort.SliceStable` checks if the lengths of the two strings are equal. If they are, it compares the strings lexicographically. If they are not, it compares their lengths. This ensures that strings with the same length are sorted alphabetically.

Then, we create a new list `result` and iterate over the sorted list of strings. For each string, we check if its length is even. If it is, we add it to the `result` list.

Finally, we return the `result` list, which contains the strings with even lengths in a sorted order. 

This function assumes that all words will have the same length, which is not the case according to the problem description. However, the function still works correctly because the problem description does not specify any conditions for the lengths of the words. The function will work correctly even if the lengths of the words are not the same. 

The time complexity of this function is O(n log n) due to the sorting, where n is the number of strings in the input list. The space complexity is O(n) for the `result` list. 





The unit tests provided ensure that the function works correctly. The test `assert list_sort(["aa", "a", "aaa"]) => ["aa"]` checks that the function removes the strings with odd lengths and returns the resulted list in a sorted order