    count := 0
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            firstDigit := str[0:1]
            lastDigit := str[len(str)-1:]
            if firstDigit == "1" || firstDigit == "3" || firstDigit == "5" || firstDigit == "7" || firstDigit == "9" {
                if lastDigit == "1" || lastDigit == "3" || lastDigit == "5" || lastDigit == "7" || lastDigit == "9" {
                    count++
                }
            }
        }
    }
    return count
}



