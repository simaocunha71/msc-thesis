    var odd_numbers []int

    current := n
    for current != 1 {
        if current%2 == 1 {
            odd_numbers = append(odd_numbers, current)
        }
        if current%2 == 0 {
            current = current / 2
        } else {
            current = current * 3 + 1
        }
    }
    odd_numbers = append(odd_numbers, 1)
    sort.Ints(odd_numbers)
    return odd_numbers
}



