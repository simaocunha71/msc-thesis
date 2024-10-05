```go
func MakeAPile(n int) []int {
    result := make([]int, n)
    stones := 1
    for i := 0; i < n; i++ {
        result[i] = stones
        if i % 2 == 0 {
            stones += 1
        } else {
            stones += 2
        }
    }
    return result
}
```


This function uses a loop to calculate the number of stones in each level. It starts with 1 stone and then adds either 1 or 2 to the number of stones for each subsequent level, depending on whether the level number is even or odd. The result is a slice of integers where each element represents the number of stones in the corresponding level. The function uses the modulo operator (`%`) to check whether the level number is even or odd. If the level number is even, it adds 1 to the number of stones; if the level number is odd, it adds 2. The result is returned as a slice of integers.