Here is the solution for the problem:

```go
func Exchange(lst1, lst2 []int) string {
    var evenCount int
    for _, num := range lst1 {
        if num%2 == 0 {
            evenCount++
        }
    }
    if evenCount == len(lst1) {
        return "YES"
    }
    for _, num := range lst2 {
        if num%2 == 0 {
            evenCount++
        }
        if evenCount == len(lst1) {
            return "YES"
        }
    }
    return "NO"
}
```


This function works by first counting the number of even numbers in lst1. If that count is equal to the length of lst1, then it is possible to make all elements of lst1 even by exchanging elements with lst2.

If it is not possible to make all elements of lst1 even by counting the even numbers in lst1, then the function iterates over the elements of lst2, counting the even numbers in lst2. If the count of even numbers in lst2 is equal to the length of lst1, then it is possible to make all elements of lst1 even by exchanging elements with lst2.

If the function has not returned "YES" by the end of the iteration, then it is not possible to make all elements of lst1 even, and the function returns "NO".