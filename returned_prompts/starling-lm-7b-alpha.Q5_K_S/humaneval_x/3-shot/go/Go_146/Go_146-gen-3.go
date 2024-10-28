    result := 0
    for _, num := range nums {
        if num > 10 {
            num_str := strconv.Itoa(num)
            if num_str[0] % 2 != 0 && num_str[len(num_str)-1] % 2 != 0 {
                result += 1
            }
        }
    }
    return result
}



