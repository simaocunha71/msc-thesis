    result := make([]int, 0)
    for _, num := range numbers {
        result = append(result, num)
        result = append(result, delimeter)
    }
    return result[:len(result)-1]
} // or return result
// or return result[:len(result)-1] to remove the extra delimeter at the end
} // or return result[1:] to remove the extra delimeter at the end


