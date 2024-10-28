    count := 0
    for i := 0; i < len(lst); i++ {
        for j := 0; j < len(lst[i]); j++ {
            if lst[i][j] == '(' {
                count += 1
            }else {
                count -= 1
            }
            if count < 0 {
                return "No"
            }
        }
    }
    if count == 0 {
        return "Yes"
    }
    return "No"
}

