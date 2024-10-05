    prime_nums := []int{2, 3, 5, 7, 11, 13, 17}
    result := 0
    for _, c := range num {
        switch {
        case c >= '0' && c <= '9':
            if contains(prime_nums, int(c-'0')) {
                result += 1
            }
        case c >= 'A' && c <= 'F':
            if contains(prime_nums, int(c-'A'+10)) {
                result += 1
            }
        }
    }
    return result
}



