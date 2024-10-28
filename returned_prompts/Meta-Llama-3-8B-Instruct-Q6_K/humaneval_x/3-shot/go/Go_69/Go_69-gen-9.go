    maxCount := 0
    maxNum := 0

    for _, num := range lst {
        count := 0
        for _, v := range lst {
            if v == num {
                count++
            }
        }
        if count >= num && count > maxCount {
            maxCount = count
            maxNum = num
        }
    }

    if maxCount >= maxNum {
        return maxNum
    } else {
        return -1
    }
}