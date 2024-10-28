    count  := 0
    for _, v  := range nums {
        if v > 10 {
            strV := strconv.Itoa(v)
            firstDigit := strV[0:1]
            lastDigit := strV[len(strV)-1:]
            if firstDigit == "1" || firstDigit == "3" || firstDigit == "5" || firstDigit == "7" || firstDigit == "9" && lastDigit == "1" || lastDigit == "3" || lastDigit == "5" || lastDigit == "7" || lastDigit == "9" {
                count++
            }
        }
    }
    return count
}


