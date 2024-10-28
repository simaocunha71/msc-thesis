    result := 0
    for _, num := range nums {
        int_str := strconv.Itoa(num)
        if int_str[0]%2 == 1 && int_str[len(int_str)-1]%2 == 1 && num > 10 {
            result++
        }
    }
    return result
}



