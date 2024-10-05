```
func Tri(n int) []float64 {
    if n == 0 {
        return []float64{}
    }
    if n == 1 {
        return []float64{3.0}
    }
    if n == 2 {
        return []float64{3.0, 2.0}
    }
    result := []float64{3.0, 2.0}
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result = append(result, 1.0+i/2.0)
        } else {
            next := result[i-1] + result[i-2] + 1.0 + (i+1)/2.0
            result = append(result, next)
        }
    }
    return result
}
```
The Tribonacci sequence is a sequence of numbers in which each number is the sum of the three preceding numbers, except for the first three numbers which are 3, 2, and 1, respectively. The sequence starts like this: 3, 2, 1, 4, 7, 13, 24, 44, 81, 149, 274, ...

In this problem, we are asked to write a function that returns the first n + 1 numbers of the Tribonacci sequence. 

Here is the solution in Go:

```go
func Tri(n int) []float64 {
    if n == 0 {
        return []float64{}
    }
    if n == 1 {
        return []float64{3.0}
    }
    if n == 2 {
        return []float64{3.0, 2.0}
    }
    result := []float64{3.0, 2.0}
    for i := 3; i <= n; i++ {
        if i%2 == 0 {
            result = append(result, 1.0+i/2.0)
        } else {
            next := result[i-1] + result[i-2] + 1.0 + (i+1)/2.0
            result = append(result, next)
        }
    }
    return result
}
```

This function first checks the base cases where n is 0, 1, or 2. Then it initializes a result slice with the first two elements of the Tribonacci sequence. It then enters a loop that