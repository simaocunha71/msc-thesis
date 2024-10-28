// Write your code here
} // HexKey function

Solution:

You can solve this problem by iterating over each character in the input string, converting it to its decimal equivalent, and checking if it's a prime number. Here's a possible implementation in Go:

```go
func HexKey(num string) int {
    count := 0
    primeNumbers := []int{2, 3, 5, 7, 11, 13, 17}
    
    for _, c := range num {
        switch c {
        case '2', 'B':
            count++
        case '3', 'D':
            count++
        case '5', '7':
            count++
        }
    }
    
    return count
}
```

In this code, we define a function `HexKey` that takes a string `num` as input. We initialize a variable `count` to 0, which will store the count of prime hexadecimal digits. We also define a slice `primeNumbers` that contains the prime numbers we're interested in.

We then iterate over each character `c` in the input string `num` using a range loop. We use a switch statement to check the value of `c`. If `c` is '2', 'B', '3', 'D', '5', or '7', we increment the `count` by 1.

Finally, we return the `count` at the end of the function. This will give us the total count of prime hexadecimal digits in the input string.

You can test this function with the examples provided in the problem statement to see that it produces the correct output. For example, `HexKey("AB")` should return 1, `HexKey("1077E")` should return 2, and so on.