    var digits []int = make([]int,0)
    for x != 0 {
        digits = append(digits,x%10)
        x /= 10
    }

    if len(digits) <= shift {
        for i := 0; i < len(digits); i++ {
            digits[i] = digits[len(digits)-1-i]
        }
        result := ""
        for _, v := range digits {
            result += strconv.Itoa(v)
        }
        return result
    }

    for i := 0; i < len(digits); i++ {
        if i < shift {
            digits[i] = digits[i+1]
        }else if i == shift {
            digits[i] = digits[0]
        }else{
            digits[i] = digits[i-1]
        }
    }

    result := ""
    for _, v := range digits {
        result += strconv.Itoa(v)
    }
    return result
}



