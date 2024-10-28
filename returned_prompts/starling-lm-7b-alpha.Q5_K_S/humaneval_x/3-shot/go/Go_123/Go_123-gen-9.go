    result := make([]int, 0)
    sequence := make([]int, 0)
    sequence = append(sequence, n)
    result = append(result, n)

    for len(sequence) > 0 {
        current := sequence[0]
        sequence = sequence[1:]
        if current % 2 == 0 {
            current = current / 2
        }else {
            current = 3 * current + 1
        }
        if current != 1 {
            sequence = append(sequence, current)
        }else{
            result = append(result, current)
        }
    }
    sort.Ints(result)
    return result
}



