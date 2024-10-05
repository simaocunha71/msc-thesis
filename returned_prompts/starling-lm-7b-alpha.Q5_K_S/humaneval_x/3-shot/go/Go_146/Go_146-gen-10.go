    result := 0
    for _, n := range nums {
        str_num := strconv.Itoa(n)
        if str_num[0]%2 == 1 && str_num[len(str_num)-1]%2 == 1 && n > 10 {
            result += 1
        }
    }
    return result
}



