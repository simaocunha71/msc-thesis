    count := 0
    for _, num := range nums {
        if num > 10 && (num%10)%2 == 1 && (num/10)%2 == 1 {
            count++
        }
    }
    return count
}



