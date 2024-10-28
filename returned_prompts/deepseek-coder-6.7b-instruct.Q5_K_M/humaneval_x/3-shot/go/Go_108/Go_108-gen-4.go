    count := 0

    for _, num := range arr {
        sum := 0
        str := strconv.Itoa(num)

        for _, char := range str {
            intChar, _ := strconv.Atoi(string(char))
            sum += intChar
        }

        if sum > 0 {
            count++
        }
    }

    return count
}



