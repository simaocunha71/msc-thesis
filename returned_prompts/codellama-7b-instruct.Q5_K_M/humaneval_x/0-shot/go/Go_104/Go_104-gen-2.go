    // Your code here
    // You can use sort.IntSlice.Filter to filter out even numbers
    // and then sort the resulting slice.
    //
    // For example, to filter out even numbers:
    //     sort.IntSlice(x).Filter(func(i int) bool { return i%2 == 1 })
    //
    // See the Go documentation for sort.IntSlice.Filter for details.
    sort.Ints(x)
    for i, v := range x {
        if v%2 == 0 {
            x = append(x[:i], x[i+1:]...)
        }
    }
    return x
}
