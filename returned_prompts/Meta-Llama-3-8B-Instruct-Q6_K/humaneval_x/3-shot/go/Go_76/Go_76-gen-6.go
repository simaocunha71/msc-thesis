    var y int = 1
    for {
        if math.Pow(float64(n), float64(y)) == float64(x) {
            return true
        }
        if math.Pow(float64(n), float64(y)) > float64(x) {
            return false
        }
        y++
    }
}