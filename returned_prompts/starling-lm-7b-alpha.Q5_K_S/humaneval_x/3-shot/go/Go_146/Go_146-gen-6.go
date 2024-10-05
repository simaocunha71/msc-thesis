    count := 0
    for _, value := range nums {
        num := strconv.Itoa(value)
        if len(num) < 2 {
            continue
        }
        if num[0] != '1' && num[0] != '3' && num[0] != '5' && num[0] != '7' && num[0] != '9' {
            continue
        }
        if num[len(num)-1] != '1' && num[len(num)-1] != '3' && num[len(num)-1] != '5' && num[len(num)-1] != '7' && num[len(num)-1] != '9' {
            continue
        }
        if value > 10 {
            count += 1
        }
    }
    return count
}



