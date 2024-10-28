```go
func Unique(l []int) []int {
    sort.Slice(l, func(i, j int) bool {
        return l[i] < l[j]
    })
    unique := []int{l[0]}
    for i := 1; i < len(l); i++ {
        if l[i] != l[i-1] {
            unique = append(unique, l[i])
        }
    }
    return unique
}
```

I have written a function that sorts a list of integers in ascending order and removes any duplicates. The function takes a slice of integers as input and returns a new slice with the unique elements. Here's the code:

```go
func Unique(l []int) []int {
    sort.Slice(l, func(i, j int) bool {
        return l[i] < l[j]
    })
    unique := []int{l[0]}
    for i := 1; i < len(l); i++ {
        if l[i] != l[i-1] {
            unique = append(unique, l[i])
        }
    }
    return unique
}
```

The function first sorts the input slice using the `sort.Slice` function and a custom comparator that compares two elements by their values. Then, it initializes a new slice called `unique` with the first element of the sorted slice. It iterates over the sorted slice starting from the second element and appends any element that is different from the previous element to the `unique` slice. Finally, it returns the `unique` slice.

You can use this function to remove duplicates from any slice of integers, like this:

```go
numbers := []int{5, 3, 5, 2, 3, 3, 9, 0, 123}
uniqueNumbers := Unique(numbers)
fmt.Println(uniqueNumbers) // Output: [0 2 3 5 9 123]
```

This will print the sorted unique elements of the `numbers` slice.