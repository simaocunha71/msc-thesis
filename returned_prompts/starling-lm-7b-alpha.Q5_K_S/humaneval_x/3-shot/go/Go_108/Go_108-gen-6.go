    count := 0
    for _,num := range arr {
        if SumDigits(num) > 0 {
            count += 1
        }
    }
    return count
}



