    result := 0
    for _, num := range nums {
        num_str := strconv.Itoa(num)
        if num > 10 && num_str[0] != '1' && num_str[len(num_str)-1] != '1' && (num_str[0] != '0' || num_str[len(num_str)-1] != '0') {
            result += 1
        }
    }
    return result
}



