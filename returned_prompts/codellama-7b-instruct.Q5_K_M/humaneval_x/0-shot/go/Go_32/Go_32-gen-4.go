    for i, x := range xs {
        if x == 0 {
            continue A
        }
        if x < 0 {
            return math.Copysign(math.Abs(math.Cbrt(x)), x)
        }
        if x > 0 {
            return math.Copysign(math.Abs(math.Cbrt(-x)), -x)
        }
    }
    return math.Copysign(math.Abs(math.Cbrt(xs[len(xs)-1])), xs[len(xs)-1])
}


func main() {
    xs := []int{1, 2}
    fmt.Println("round(FindZero([1, 2]), 2) # f(x) = 1 + 2x")
    fmt.Println("-0.5")
    fmt.Println("round(FindZero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3")
    fmt.Println("1.0")
    fmt.Println(round(FindZero(xs), 2))
}

func round(val float64, places int) float64 {
    shift := math.Pow(10, float64(places))
    return math.Floor(val*shift+.5) / shift
}
