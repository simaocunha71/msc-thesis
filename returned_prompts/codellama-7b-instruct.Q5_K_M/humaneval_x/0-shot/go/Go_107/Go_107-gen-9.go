    for i := 1; i < n; i++ {
        if i == 1 || i == 2 {
            continue
        }
        if i%2 == 0 {
            continue
        }
        for j := 0; j < len(strconv.Itoa(i)); j++ {
            if strconv.Itoa(i)[j] != strconv.Itoa(i)[len(strconv.Itoa(i))-j-1] {
                continue A
            }
        }
        fmt.Printf("%d is palindrome\n", i)
    }
    return [2]int{1, 1}
}