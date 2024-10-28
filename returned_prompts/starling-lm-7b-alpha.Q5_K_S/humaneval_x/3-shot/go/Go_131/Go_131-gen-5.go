    result := 1
    n_s := strconv.Itoa(n)
    for _, c := range n_s {
        i, _ := strconv.Atoi(string(c))
        if i % 2 != 0 {
            result *= i
        }
    }
    return result
}




