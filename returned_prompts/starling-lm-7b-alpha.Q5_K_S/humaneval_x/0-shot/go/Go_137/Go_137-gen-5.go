    // Type assertions to convert the values to their basic types
    f := a.(float64)
    s := b.(string)
    i := int(f)

    if i == f {
        if i == strconv.ParseFloat(s, 64) {
            return nil
        }
        if strconv.ParseFloat(s, 64) > f {
            return s
        }
        return f
    }

    if strconv.ParseFloat(s, 64) > f {
        return s
    }
    return f
}

// CompareOne(1, 2.5) ➞ 2.5
func CompareOne(a, b interface{}) interface{} {
    f := a.(float64)
    s := b.(string)
    i := int(f)

    if i == f {
        if i == strconv.ParseFloat(s, 64) {
            return nil
        }
        if strconv.ParseFloat(s, 64) > f {
            return s
        }
        return f
    }

    if strconv.ParseFloat(s, 64) > f {
        return s
    }
    return f
}

// CompareOne(1, "2,3") ➞ "2,3"
func CompareOne(a, b interface{}) interface{} {
    f := a.(float64)
    s := b.(string)
    i := int(f)

    if i == f {
        if i == strconv.ParseFloat(s, 64) {
            return nil
        }
        if strconv.ParseFloat(s, 64) > f {
            return s
        }
        return f
    }

    if strconv.ParseFloat(s, 64) > f {
        return s
    }
    return f
}

// CompareOne("5,1", "6") ➞ "6"
func CompareOne(a, b interface{}) interface{} {
    f := a.(float64)
    s := b.(string)
    i :=