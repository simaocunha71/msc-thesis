```go
func Add(lst []int) int {
    var sum int
    for i, v := range lst {
        if i%2 != 0 && v%2 == 0 {
            sum += v
        }
    }
    return sum
}
```


This problem asks you to create a function that takes a list of integers as input, and returns the sum of all even numbers that are at odd indices in the list.

For example, if the input list is [4, 2, 6, 7], the function should return 2, because 2 is the only even number at an odd index (index 1) in the list.

Here's a Go solution for this problem:

```go
func Add(lst []int) int {
    var sum int
    for i, v := range lst {
        if i%2 != 0 && v%2 == 0 {
            sum += v
        }
    }
    return sum
}
```

This function uses a for loop to iterate over the input list. The range function is used to iterate over the list, and it returns two values for each iteration: the index i and the value v of the current element.

Inside the loop, we check if the index i is odd (i%2 != 0) and if the value v is even (v%2 == 0). If both conditions are true, we add the value v to the sum.

Finally, the function returns the sum of all even numbers at odd indices in the list.