    // Convert all types to float
    var (
        aF float64
        bF float64
    )

    if a == nil {
        return b
    }

    if b == nil {
        return a
    }

    if aa, ok := a.(float64); ok {
        aF = aa
    } else if aa, ok := a.(float32); ok {
        aF = float64(aa)
    } else if str, ok := a.(string); ok {
        aF, _ = strconv.ParseFloat(str, 64)
    } else {
        aF = float64(a)
    }

    if bb, ok := b.(float64); ok {
        bF = bb
    } else if bb, ok := b.(float32); ok {
        bF = float64(bb)
    } else if str, ok := b.(string); ok {
        bF, _ = strconv.ParseFloat(str, 64)
    } else {
        bF = float64(b)
    }

    if aF > bF {
        return aF
    } else if aF == bF {
        return nil
    } else {
        return bF
    }
}

func main() {
    fmt.Println(CompareOne(1, 2.5))
    fmt.Println(CompareOne(1, "2,3"))
    fmt.Println(CompareOne("5,1", "6"))
    fmt.Println(CompareOne("1", 1))
}


























































































































