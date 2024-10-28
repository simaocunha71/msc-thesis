    count := 0
    for _, n := range nums {
        if n > 10 {
            first_digit, _ := strconv.Atoi(string(strconv.Itoa(n)[0]))
            last_digit, _ := strconv.Atoi(string(strconv.Itoa(n)[len(strconv.Itoa(n))-1]))
            if first_digit%2 == 1 && last_digit%2 == 1 {
                count++
            }
        }
    }
    return count
}

