    if a == b {
        return nil
    } else if a_type, _ := a.(string); a_type != "" {
        float_a, _ := strconv.ParseFloat(a_type, 64)
        return CompareOne(float_a, b)
    } else if b_type, _ := b.(string); b_type != "" {
        float_b, _ := strconv.ParseFloat(b_type, 64)
        return CompareOne(a, float_b)
    }
    if float_a, ok := a.(float64); ok {
        if float_b, ok := b.(float64); ok {
            if float_a > float_b {
                return float_a
            } else if float_b > float_a {
                return float_b
            } else {
                return nil
            }
        } else if int_b, ok := b.(int); ok {
            if float_a > int_b {
                return float_a
            } else if int_b > float_a {
                return int_b
            } else {
                return nil
            }
        } else {
            return CompareOne(float_a, b)
        }
    } else if int_a, ok := a.(int); ok {
        if float_b, ok := b.(float64); ok {
            if float_b > int_a {
                return float_b
            } else if int_a > float_b {
                return int_a
            } else {
                return nil
            }
        } else if int_b, ok := b.(int); ok {
            if int_a > int_b {
                return int_a
            } else if int_b > int_a {
                return int_b
            } else {
                return nil
            }
        } else {
            return CompareOne(int_a, b)
        }
    }
}



