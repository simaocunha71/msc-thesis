You can solve this problem by using recursion. Here is a solution written in Go:

```go
func Intersperse(numbers []int, delimeter int) []int {
    if len(numbers) == 0 {
        return []int{}
    } else if len(numbers) == 1 {
        return numbers
    } else {
        return append(append(numbers[:1], delimeter), Intersperse(numbers[1:], delimeter)...)
    }
}
```

In this solution, the base cases are when the input list is empty (return an empty list) or when the input list has only one element (return the list as is). In the recursive case, we append the first element of the list, the delimiter, and the result of the recursive call for the rest of the list. We use the append function to concatenate lists in Go.

This solution has a time complexity of O(n), where n is the length of the input list, since we have to visit each element of the list once.