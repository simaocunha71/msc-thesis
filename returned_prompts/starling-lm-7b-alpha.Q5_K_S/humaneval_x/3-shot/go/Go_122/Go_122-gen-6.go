    sum := 0
    for i, element := range arr[:k] {
        if len(strconv.Itoa(element)) <= 2 {
            sum += element
        }
    }
    return sum
}



