    count := 0
    for _, num := range nums {
        if num > 10 {
            numStr := strconv.Itoa(num)
            if numStr[0] == "1" || numStr[0] == "3" || numStr[0] == "5" || numStr[0] == "7" || numStr[0] == "9" {
                if numStr[len(numStr)-1] == "1" || numStr[len(numStr)-1] == "3" || numStr[len(numStr)-1] == "5" || numStr[len(numStr)-1] == "7" || numStr[len(numStr)-1] == "9" {
                    count += 1
                }
            }
        }
    }
    return count
}



