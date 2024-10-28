    for i := 0; i < n; i++ {
        s := strconv.Itoa(i)
        if s == string(s[::-1]) && i%2 == 0 {
            continue A
        }
    }
    return [2]int{n-1, 0}
}
