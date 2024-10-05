    count := 0
    for _, num := range nums {
        if num > 10 {
            strNum := strconv.Itoa(int(math.Abs(float64(num))))
            firstDigit := strNum[0:1]
            lastDigit := strNum[len(strNum)-1:]
            if firstDigit == "1" || firstDigit == "3" || firstDigit == "5" || firstDigit == "7" || firstDigit == "9" &&
            lastDigit == "1" || lastDigit == "3" || lastDigit == "5" || lastDigit == "7" || lastDigit == "9" {
                count++
            }
        }
    }
    return count
}



