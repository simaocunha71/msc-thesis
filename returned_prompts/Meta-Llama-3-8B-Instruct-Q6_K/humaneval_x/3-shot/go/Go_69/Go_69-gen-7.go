    maxCount := 0
    maxNumber := -1

    countMap := make(map[int]int)

    for _, num := range lst {
        if _, ok := countMap[num]; ok {
            countMap[num]++
        } else {
            countMap[num] = 1
        }

        if countMap[num] >= num && num > maxNumber {
            maxNumber = num
            maxCount = countMap[num]
        }
    }

    if maxNumber == -1 {
        return -1
    } else {
        return maxNumber
    }
} 