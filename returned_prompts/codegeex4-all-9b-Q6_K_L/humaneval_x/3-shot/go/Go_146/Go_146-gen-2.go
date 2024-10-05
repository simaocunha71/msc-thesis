    count := 0
    for _, num := range nums {
        if num > 10 && strconv.Itoa(num)[0] % 2 == 1 && strconv.Itoa(num)[len(strconv.Itoa(num))-1] % 2 == 1{
            count += 1
        }
    }
    return count
}



