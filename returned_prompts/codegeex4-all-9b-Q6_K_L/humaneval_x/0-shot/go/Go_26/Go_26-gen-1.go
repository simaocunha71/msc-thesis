Here is a simple solution in Go:

```go
func RemoveDuplicates(numbers []int) []int {
    set := make(map[int]struct{})
    result := make([]int, 0)
    for _, num := range numbers {
        if _, found := set[num]; !found {
            set[num] = struct{}{}
            result = append(result, num)
        }
    }
    return result
}
```

This solution creates a map `set` to keep track of the unique numbers we have seen so far. It then iterates over the input slice `numbers`, and for each number, it checks if it has already been seen by looking it up in `set`. If it has not been seen, it adds it to `set` and appends it to the result slice `result`. Finally, it returns the result slice.

Note that the map `set` uses empty structs as its values, which is a common trick to make a map with only keys. This is because maps in Go are not allowed to have nil values, but empty structs are considered "zero values" and are allowed.

Also note that this solution keeps the order of the elements the same as in the input. If you want to remove duplicates while also sorting the result, you can modify the solution accordingly.