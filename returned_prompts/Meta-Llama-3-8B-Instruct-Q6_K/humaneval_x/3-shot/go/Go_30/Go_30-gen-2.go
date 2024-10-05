    var result []int
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}  // or use filter function from the Go's standard library: return Ints(l)...filter(Ints(l), func(x int) bool { return x > 0 })