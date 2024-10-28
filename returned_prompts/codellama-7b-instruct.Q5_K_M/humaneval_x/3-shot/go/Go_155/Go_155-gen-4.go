    even := 0
    odd := 0
    num_str := strconv.Itoa(num)

    for _, c := range num_str {
        digit, _ := strconv.Atoi(string(c))
        if digit%2 == 0 {
            even += 1
        } else {
            odd += 1
        }
    }
    return [2]int{even, odd}
}



