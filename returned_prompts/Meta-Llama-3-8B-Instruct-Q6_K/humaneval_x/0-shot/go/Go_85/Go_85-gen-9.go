```go
func Add(lst []int) int {
    var sum int
    for i, num := range lst {
        if i%2 != 0 && num%2 == 0 {
            sum += num
        }
    }
    return sum
}
```


Python solution:

```python
def add(lst):
    return sum(num for i, num in enumerate(lst) if i % 2 != 0 and num % 2 == 0)
```

Explanation:

*   We iterate over the list using a for loop in Go and enumerate function in Python, which gives us both the index `i` and the value `num` of each element.
*   We check if the index `i` is odd (`i % 2 != 0`) and if the value `num` is even (`num % 2 == 0`). If both conditions are true, we add `num` to our running sum `sum`.
*   Finally, we return the sum of the even elements at odd indices.

For example, given the list `[4, 2, 6, 7]`, the function will return `2` because `2` is the only even element at an odd index.