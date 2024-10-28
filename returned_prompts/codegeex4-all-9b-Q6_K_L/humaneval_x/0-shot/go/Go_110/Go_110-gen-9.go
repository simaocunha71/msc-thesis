Here is a possible solution:

```go
func Exchange(lst1, lst2 []int) string {
    // Count the number of odd numbers in lst1
    oddCount := 0
    for _, num := range lst1 {
        if num % 2 != 0 {
            oddCount++
        }
    }
    
    // Count the number of even numbers in lst2
    evenCount := 0
    for _, num := range lst2 {
        if num % 2 == 0 {
            evenCount++
        }
    }
    
    // If the number of odd numbers in lst1 is greater than the number of even numbers in lst2,
    // it is not possible to make all elements of lst1 even by exchanging elements between them.
    if oddCount > evenCount {
        return "NO"
    }
    
    // Otherwise, it is possible to make all elements of lst1 even by exchanging elements between them.
    return "YES"
}
```

The function first counts the number of odd numbers in `lst1` and the number of even numbers in `lst2`. If the number of odd numbers in `lst1` is greater than the number of even numbers in `lst2`, it is not possible to make all elements of `lst1` even by exchanging elements between them. Otherwise, it is possible to make all elements of `lst1` even by exchanging elements between them.