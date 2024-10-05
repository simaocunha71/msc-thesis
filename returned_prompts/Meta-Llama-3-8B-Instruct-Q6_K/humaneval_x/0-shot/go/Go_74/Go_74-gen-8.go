Here is the solution to the problem:

```go
func TotalMatch(lst1 []string, lst2 []string) []string {
    var sum1, sum2 int
    for _, s := range lst1 {
        sum1 += len(s)
    }
    for _, s := range lst2 {
        sum2 += len(s)
    }
    if sum1 < sum2 {
        return lst1
    } else if sum1 > sum2 {
        return lst2
    } else {
        return lst1
    }
}
```


The function `TotalMatch` takes two lists of strings as input and returns the list that has the total number of characters in all the strings of the list less than the other list. If the two lists have the same number of characters, it returns the first list. 

It calculates the total number of characters in each list and compares them. If the total number of characters in the first list is less than the second, it returns the first list. If the total number of characters in the second list is less than the first, it returns the second list. If the total number of characters in both lists is the same, it returns the first list. 

The time complexity of this function is O(n), where n is the total number of strings in both lists. This is because it iterates over each string in both lists once to calculate the total number of characters. The space complexity is O(1), as it only uses a constant amount of space to store the sums of the lengths of the strings. 