    smallest_even_val := math.MaxInt64
    smallest_even_idx := -1

    for i, num := range arr {
        if num % 2 == 0 && num < smallest_even_val {
            smallest_even_val = num
            smallest_even_idx = i
        }
    }

    if smallest_even_idx == -1 {
        return []int{}
    }

    return []int{smallest_even_val, smallest_even_idx}
}



