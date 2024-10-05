    count := 0
    for _, num := range nums {
        if num > 10 {
            strNum := strconv.Itoa(num)
            firstDigit := strNum[0:1]
            lastDigit := strNum[len(strNum)-1:]
            firstDigitInt, _ := strconv.Atoi(firstDigit)
            lastDigitInt, _ := strconv.Atoi(lastDigit)
            if firstDigitInt % 2 == 1 && lastDigitInt % 2 == 1 {
                count++
            }
        }
    }
    return count
}



