To solve this problem, we need to check if there is at least one even number in lst2. If there is, then we can perform an Exchange to make all elements in lst1 even. If there isn't, then it's not possible.

Here is the implementation in Go:

```go
func Exchange(lst1, lst2 []int) string {
    for _, num := range lst2 {
        if num%2 == 0 {
            return "YES"
        }
    }
    return "NO"
}
```

This function iterates over the elements in lst2 and checks if any of them is even. If it finds an even number, it returns "YES". Otherwise, it returns "NO".