    smallest_even_val := math.MaxInt64
    smallest_even_index := -1

    for i, v := range arr  {
        if v % 2 == 0 && v < smallest_even_val  {
            smallest_even_val = v
            smallest_even_index = i
        }
    }

    if smallest_even_index == -1  {
        return []int{}
    }else {
        return []int{smallest_even_val, smallest_even_index}
    }
}



