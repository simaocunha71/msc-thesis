    numbers := strings.Split(s, " ")
    for i:= range numbers {
        numbers[i] = strings.Trim(numbers[i], " apples and oranges")
    }
    sum := 0
    for _, number := range numbers {
        num, _ := strconv.Atoi(number)
        sum += num
    }

    return n - sum
}




