    var max_negative int64
    var min_positive int64
    var has_negative bool
    var has_positive bool

    for _, num := range lst {
        if num < 0 {
            if max_negative == 0 || int64(num) > max_negative {
                max_negative = int64(num)
            }
            has_negative = true
        } else if num > 0 {
            if min_positive == 0 || int64(num) < min_positive {
                min_positive = int64(num)
            }
            has_positive = true
        }
    }

    if has_negative && has_positive {
        return [2]interface{}{max_negative, min_positive}
    } else if has_negative {
        return [2]interface{}{max_negative, nil}
    } else if has_positive {
        return [2]interface{}{nil, min_positive}
    } else {
        return [2]interface{}{nil, nil}
    }
}  // or 
func LargestSmallestIntegers(lst []int) [2]interface{} {
    var result [2]interface{}
    max_negative, min_positive := int64(math.MaxInt32), int64(math.MinInt32)
    has_negative, has_positive := false, false

    for _, num := range lst {
        if num < 0 {
            if num > int64(int32(max_negative)) {
                max_negative = int64(num)
            }
            has_negative = true
        } else if num > 0 {
            if num < min_positive {
                min_positive = int64(num)
            }
            has_positive = true
        }
    }

    if has_negative && has_positive {
        result[0] = max_negative
        result[1] = min_positive
    } else if has_negative {
        result[0] = max_negative
        result[1] = nil
    } else if has_positive {
        result[0] = nil
        result[1] = min_positive
    } else {
        result[0] = nil
        result[1] = nil
    }

    return result
}  // or 
func LargestSmallestIntegers(lst []int) [2]interface{} {
    var result [2]interface{}
    var max_negative, min_positive int

    for _, num := range lst {
        if num < 0 {
            if max_negative < num {
                max_negative = num
            }
        } else if num > 0 {
            if min_positive >