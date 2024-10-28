    count := 0
    for _, num := range nums {
        if num > 10 {
            strNum := strconv.Itoa(num)
            if strNum[0] % 2 == 1 && strNum[len(strNum)-1] % 2 == 1 {
                count++
            }
        }
    }
    return count
}



