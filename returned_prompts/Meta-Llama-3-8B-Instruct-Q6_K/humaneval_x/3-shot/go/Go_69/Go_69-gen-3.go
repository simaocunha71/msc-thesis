    maxCount := 0
    maxNum := -1
    count := make(map[int]int)

    for _, num := range lst {
        if _, ok := count[num]; ok {
            count[num] += 1
        } else {
            count[num] = 1
        }
        if count[num] >= num && num > maxNum {
            maxNum = num
            maxCount = count[num]
        }
    }
    if maxNum == -1 {
        return -1
    } else {
        return maxNum
    }
} 





