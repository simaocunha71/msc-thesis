    result := 0
    for _, num := range nums {
        if num > 10 && num%2 == 1 {
            first_str := strconv.Itoa(num/10)
            last_str := strconv.Itoa(num%10)
            if first_str[0] == '1' || first_str[0] == '3' || first_str[0] == '5' || first_str[0] == '7' || first_str[0] == '9' && last_str[0] == '1' || last_str[0] == '3' || last_str[0] == '5' || last_str[0] == '7' || last_str[0] == '9' {
                result += 1
            }
        }
    }
    return result
}



