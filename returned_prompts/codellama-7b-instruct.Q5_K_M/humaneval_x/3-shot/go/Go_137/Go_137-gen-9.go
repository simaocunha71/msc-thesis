    switch a.(type) {
    case string:
        as := a.(string)
        bs := b.(string)

        if as == bs {
            return nil
        }

        var as_float, bs_float float64
        var err1, err2 error
        as_float, err1 = strconv.ParseFloat(as, 64)
        bs_float, err2 = strconv.ParseFloat(bs, 64)

        if err1 != nil || err2 != nil {
            panic(err1)
        }

        if as_float > bs_float {
            return a
        } else {
            return b
        }

    case int, float32, float64:
        af := a.(float64)
        bf := b.(float64)

        if af == bf {
            return nil
        }

        if af > bf {
            return a
        } else {
            return b
        }

    default:
        panic(fmt.Sprintf("unsupported type %T", a))
    }
}



