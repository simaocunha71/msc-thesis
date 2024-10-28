 
var result = make([]int, n)
for i := range result {
    if i%2 == 0 {
        result[i] = factorial(i)
    } else {
        result[i] = sum(i)
    }
}
return result
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}

func sum(n int) int {
    sum := 0
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}

```

This program defines a function F which generates a list of length n according to the rules provided in the question. It uses two helper functions factorial and sum to compute the factorial of a number and the sum of numbers from 1 to a number respectively. In the main function F, it iterates over the range of n and checks if the index is even or odd. If the index is even, it calculates the factorial of the index, otherwise it calculates the sum of numbers from 1 to the index. The result is then stored in the result list.

Please note: The recursive implementation of the factorial function in the provided solution might not work for larger inputs due to the limitations of the recursion depth in Go. For such cases, you might want to use an iterative implementation of the factorial function.
Also, please note that Go is a statically typed language and the type of n is not specified in the function definition.

This code assumes that the input n is a non-negative integer. If n can be a negative number or a floating point number, you need to handle those cases as well.

Also, it's worth mentioning that the time complexity of this program is O(n^2) due to the usage of factorial and sum functions inside the loop. It's not efficient but it's the best solution we have without modifying the problem statement.

This code can be compiled and run with any Go compiler. Just copy the code into a file and run it with the command `go run filename.go`.

```

```



```go
// This program returns the factorial of a number
func