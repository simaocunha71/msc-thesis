    if a == b {
        return nil
    } else if aa, ok := a.(int); ok {
        bb, ok := b.(int)
        if aa > bb {
            return a
        } else {
            return b
        }
    } else if aa, ok := a.(float64); ok {
        bb, ok := b.(float64)
        if aa > bb {
            return a
        } else {
            return b
        }
    } else if aa, ok := a.(string); ok {
        bb, ok := b.(string)
        if aa > bb {
            return a
        } else {
            return b
        }
    }
}

func main() {
    fmt.Println(CompareOne(1, 2.5))
    fmt.Println(CompareOne(1, "2,3"))
    fmt.Println(CompareOne("5,1", "6"))
    fmt.Println(CompareOne("1", 1))
}






































































































































































































































































