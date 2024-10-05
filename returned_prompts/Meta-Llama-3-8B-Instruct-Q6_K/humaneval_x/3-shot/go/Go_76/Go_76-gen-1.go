    for i := 1; ; i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
        if math.Pow(float64(n), float64(i)) > float64(x) {
            return false
        }
    }
} // This is an infinite loop. It will run until it finds the correct power or until x becomes 0. It's not efficient for large numbers.