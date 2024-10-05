```go
func Exchange(lst1, lst2 []int) string {
    evenCount := 0
    for _, v := range lst1 {
        if v%2 == 0 {
            evenCount++
        }
    }
    if evenCount == len(lst1) {
        return "YES"
    }
    for _, v := range lst2 {
        if v%2 == 0 {
            evenCount++
        }
    }
    if evenCount == len(lst1) {
        return "YES"
    }
    return "NO"
}
```


Here is the explanation of the solution:

The function `Exchange` takes two lists of numbers `lst1` and `lst2` as input. It first counts the number of even numbers in `lst1` and stores this count in `evenCount`. If `evenCount` is equal to the length of `lst1`, it means that all elements in `lst1` are even, so it returns "YES". Otherwise, it counts the number of even numbers in `lst2`. If `evenCount` becomes equal to the length of `lst1` after counting the even numbers in `lst2`, it means that it is possible to make all elements in `lst1` even by exchanging elements with `lst2`, so it returns "YES". If `evenCount` is still less than the length of `lst1` after counting the even numbers in `lst2`, it means that it is not possible to make all elements in `lst1` even by exchanging elements with `lst2`, so it returns "NO".