    var max int
    for _, i := range l {
        if i > max {
            max = i
        }
    }
    return max
}  // or return math.MaxInt for int32, or math.MaxInt64 for int64
} // or return math.MaxFloat for float64, or math.MaxFloat64 for float64

