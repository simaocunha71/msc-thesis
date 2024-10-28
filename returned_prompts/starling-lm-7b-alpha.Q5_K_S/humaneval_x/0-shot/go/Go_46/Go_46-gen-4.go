
```go
var (
    fib = []int{0, 0, 2, 0}
    nth = []int{0, 1, 2, 3}
)

func Fib4(n int) int {
    if n < len(fib) {
        return fib[n]
    }
    for fibLen := len(fib); nth[n-fibLen] == 0 && nth[n-fibLen-1] == 0; nth[n-fibLen], nth[n-fibLen-1] = 0, 1 {
        fib = append(fib, fib[nth[n-fibLen]-1]+fib[nth[n-fibLen-1]-1]+fib[nth[n-fibLen-2]-1]+fib[nth[n-fibLen-3]-1])
    }
    return fib[n]
}
```

To efficiently compute the n-th element of the Fib4 number sequence, we maintain a slice fib that holds the first four elements of the sequence, and a slice nth that holds the indices of the first four elements of the sequence. We start by checking if n is less than the length of the fib slice. If it is, we can simply return the element at the nth index in the fib slice.

If n is greater than or equal to the length of the fib slice, we enter a loop that iterates until we reach the end of the sequence (i.e., until nth[n-fibLen] == 0 && nth[n-fibLen-1] == 0). Within the loop, we update the values in the fib and nth slices based on the values of the previous elements in the fib slice. Specifically, we set nth[n-fibLen] to 0 and nth[n-fibLen-1] to 1, and append the sum of the previous four elements in the fib slice to the fib slice.

Finally, we return the nth element of the fib slice, which is the value we computed in the loop.

The time complexity of this solution is O(n) because we perform at most four