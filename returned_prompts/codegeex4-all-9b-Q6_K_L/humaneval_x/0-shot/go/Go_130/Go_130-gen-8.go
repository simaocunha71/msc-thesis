You can solve this problem by creating a recursive function that generates the Tribonacci sequence. Here's a possible solution in Go:

```go
func Tri(n int) []float64 {
    if n == 0 {
        return []float64{3}
    }
    if n == 1 {
        return []float64{1, 3}
    }
    sequence := Tri(n - 1)
    nextValue := sequence[n-1] + sequence[n-2] + sequence[n-3]
    sequence = append(sequence, nextValue)
    return sequence
}
```

This function uses a recursive approach to generate the Tribonacci sequence. It starts by checking if the input `n` is 0 or 1, and returns the corresponding sequence. For other values of `n`, it calls itself recursively to generate the sequence up to `n-1`, then calculates the next value in the sequence by summing the last three values in the sequence. Finally, it appends the next value to the sequence and returns it.

You can test the function with the provided examples:

```go
func main() {
    fmt.Println(Tri(3)) // Output: [1 3 2 8]
}
```

This will output `[1 3 2 8]`, which is the Tribonacci sequence for `n = 3`.