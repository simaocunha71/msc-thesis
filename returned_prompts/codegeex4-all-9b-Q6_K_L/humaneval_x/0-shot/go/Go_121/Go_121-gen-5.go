func Solution(lst []int) int {
    s := 0
    for i, v := range lst {
        if i % 2 == 1 && v % 2 == 1 {
            s += v
        }
    }
    return s
}

or

func Solution(lst []int) int {
    s := 0
    for i := 1; i < len(lst); i += 2 {
        if lst[i] % 2 == 1 {
            s += lst[i]
        }
    }
    return s
}