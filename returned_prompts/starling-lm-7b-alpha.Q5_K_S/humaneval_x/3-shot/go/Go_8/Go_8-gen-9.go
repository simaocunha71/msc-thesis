    result := [2]int{0, 1}

    for _, number := range numbers {
        result[0] += number
        result[1] *= number
    }

    return result
}



