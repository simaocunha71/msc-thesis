    count := 0
    for _, num := range nums {
        if num > 10 {
            str := strconv.Itoa(num)
            first := str[0]
            last := str[len(str)-1]
            if first % 2 == 1 && last % 2 == 1 {
                count++
            }
        }
    }
    return count
}



