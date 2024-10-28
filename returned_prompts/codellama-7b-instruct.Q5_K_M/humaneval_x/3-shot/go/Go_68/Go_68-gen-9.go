    var smallest_value int
    var smallest_index int
    var has_smallest bool

    for i, v := range arr {
        if v%2 == 0 {
            if has_smallest {
                if v < smallest_value {
                    smallest_value = v
                    smallest_index = i
                }
            } else {
                smallest_value = v
                smallest_index = i
                has_smallest = true
            }
        }
    }
    if has_smallest {
        return []int{smallest_value, smallest_index}
    }

    return []int{}
}



