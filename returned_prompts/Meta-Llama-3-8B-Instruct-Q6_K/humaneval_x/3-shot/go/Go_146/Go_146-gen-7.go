    count := 0
    for _, num := range nums {
        if num > 10 {
            strNum := strconv.Itoa(num)
            if (int(strNum[0]-'0') % 2 != 0) && (int(strNum[len(strNum)-1]-'0') % 2 != 0) {
                count++
            }
        }
    }
    return count
}