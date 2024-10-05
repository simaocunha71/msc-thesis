Here is the solution:

```go
func TriplesSumToZero(l []int) bool {
    for i := 0; i < len(l)-2; i++ {
        for j := i + 1; j < len(l)-1; j++ {
            for k := j + 1; k < len(l); k++ {
                if l[i]+l[j]+l[k] == 0 {
                    return true
                }
            }
        }
    }
    return false
}
```

Explanation:

This solution uses three nested loops to iterate through all possible combinations of three elements in the list. For each combination, it checks if their sum is zero. If a combination is found that sums to zero, the function returns true. If no such combination is found after checking all possible combinations, the function returns false.