You can solve this problem by determining if there is at least one even number in lst2 and if lst1 has any odd numbers. If both conditions are true, then it is possible to perform an Exchange to make lst1 a list of only even numbers. Otherwise, it is not possible.

Here is the implementation of the Exchange function in Go:

```go
func Exchange(lst1, lst2 []int) string {
    hasEven := false
    hasOdd := false

    for _, num := range lst1 {
        if num%2 == 1 {
            hasOdd = true
        }
    }

    for _, num := range lst2 {
        if num%2 == 0 {
            hasEven = true
        }
    }

    if hasEven && hasOdd {
        return "YES"
    }

    return "NO"
}
```

In this implementation, we initialize two boolean variables, hasEven and hasOdd, to false. Then, we iterate over lst1 and lst2 to check if there is any odd number in lst1 and any even number in lst2. If there is at least one odd number in lst1 and at least one even number in lst2, we return "YES". Otherwise, we return "NO".