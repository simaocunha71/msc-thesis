```
func Fib4(n int) int {
    if n <= 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }
    fib4 := [4]int{0, 0, 2, 0}
    for i := 4; i <= n; i++ {
        fib4[i % 4] = fib4[(i-1)%4] + fib4[(i-2)%4] + fib4[(i-3)%4] + fib4[(i-4)%4]
    }
    return fib4[n % 4]
}
```


The function takes an integer `n` as input and returns the `n-th` element of the Fib4 sequence. The function uses a technique called "circular array" to store the previous four elements of the sequence. This allows us to calculate the `n-th` element in constant time.

Here's a step-by-step breakdown of how the function works:

1. If `n` is 0 or 1, return 0, since Fib4(0) and Fib4(1) are both 0.
2. If `n` is 2, return 2, since Fib4(2) is 2.
3. If `n` is 3, return 0, since Fib4(3) is 0.
4. Create a circular array `fib4` of size 4, initialized with the values {0, 0, 2, 0}. This array will store the previous four elements of the sequence.
5. Iterate from `i = 4` to `n`, and for each `i`, calculate the `i-th` element of the sequence using the previous four elements. This is done by taking the sum of the previous four elements modulo 4, which allows us to wrap around the circular array.
6. Return the `n-th` element of the sequence, which is stored in the `fib4` array at index `n % 4`.

The time complexity of this function is O(1), since we only need to iterate a constant number of times to calculate the `n-th` element. The space complexity is O(1), since we only need to store a constant number of elements in the `fib4` array.