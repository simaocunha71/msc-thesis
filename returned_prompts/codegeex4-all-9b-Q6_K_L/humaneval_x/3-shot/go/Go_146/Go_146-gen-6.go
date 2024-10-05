    result := 0
    for _, number := range nums{
        if number > 10 && number % 2 != 0 {
            str := strconv.Itoa(number)
            first_digit,_ := strconv.Atoi(string(str[0]))
            last_digit,_ := strconv.Atoi(string(str[len(str)-1]))

            if first_digit % 2 != 0 && last_digit % 2 != 0 {
                result += 1
            }
        }
    }
    return result
}

