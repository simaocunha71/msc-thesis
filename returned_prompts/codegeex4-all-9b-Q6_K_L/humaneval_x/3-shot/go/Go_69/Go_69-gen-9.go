    frequency := make(map[int]int)
    for _, number := range lst {
        frequency[number] += 1
    }

    var greatest int = -1
    for number, count := range frequency {
        if count >= number && number > greatest {
            greatest = number
        }
    }
    return greatest
}



