This is a simple task which can be solved by checking the parity of each element in both lists and counting the number of odd elements in each list. If the total number of odd elements in both lists is even, then it is possible to make all elements in lst1 even by exchanging elements between lst1 and lst2. Otherwise, it is not possible.

The algorithm is as follows:

- Count the number of odd elements in lst1.
- Count the number of odd elements in lst2.
- If the sum of the number of odd elements in lst1 and lst2 is even, return "YES".
- Otherwise, return "NO".

Here is the implementation in Go:

```go
func Exchange(lst1, lst2 []int) string {
    oddCount1, oddCount2 := 0, 0
    for _, num := range lst1 {
        if num%2 != 0 {
            oddCount1++
        }
    }
    for _, num := range lst2 {
        if num%2 != 0 {
            oddCount2++
        }
    }
    if (oddCount1+oddCount2)%2 == 0 {
        return "YES"
    }
    return "NO"
}
```

This function takes two slices of integers as input and returns a string. It first counts the number of odd elements in lst1 and lst2 using the range loop. Then it checks whether the sum of the number of odd elements in lst1 and lst2 is even. If it is, it returns "YES". Otherwise, it returns "NO".