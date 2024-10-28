    count := 0
    for _, num := range nums {
        if num > 10 {
            strNum := strconv.Itoa(num)
            firstDigit := strNum[0]
            lastDigit := strNum[len(strNum)-1]
            if firstDigit%2 == 1 && lastDigit%2 == 1 {
                count++
            }
        }
    }
    return count
}



