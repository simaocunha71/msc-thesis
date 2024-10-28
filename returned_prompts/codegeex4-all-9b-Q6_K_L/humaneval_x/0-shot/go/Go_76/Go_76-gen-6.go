package kata

func IsSimplePower(x int,n int) bool {
    for i := 1; i <= x; i++ {
        if i * i == x {
            return true
        }
    }
    return false
}

// func IsSimplePower(x int,n int) bool {
//     for i := 1; i <= x; i++ {
//         if math.Pow(float64(i), float64(n)) == float64(x) {
//             return true
//         }
//     }
//     return false
// }

func IsSimplePower2(x int,n int) bool {
    for i := 1; i <= x; i++ {
        if i * i == x {
            return true
        }
    }
    return false
}

func IsSimplePower3(x int,n int) bool {
    if math.Pow(float64(n), 1/float64(x)) == float64(x) {
        return true
    }
    return false
}

func IsSimplePower4(x int,n int) bool {
    if math.Pow(float64(x), 1/float64(n)) == float64(n) {
        return true
    }
    return false
}

func IsSimplePower5(x int,n int) bool {
    if math.Pow(float64(n), 1/float64(x)) == float64(n) {
        return true
    }
    return false
}

func IsSimplePower6(x int,n int) bool {
    if math.Pow(float64(x), 1/float64(n)) == float64(x) {
        return true
    }
    return false
}

func IsSimplePower7(x int,n int) bool {
    if math.Pow(float64(n), 1/float64(x)) == float64(x) {
        return true
    }
    return false
}

func IsSimplePower8(x int,n int) bool {
    if math.Pow(float64(x), 1/float64(n)) == float64(n) {
        return true
    }
    return false
}

func IsSimplePower9(x int,n int) bool {
    if math.Pow(float64(n), 1/float64(x)) == float64(x) {
        return true
    }
    return false
}

func IsSimplePower10(x int,n int) bool {
    if math.Pow(float64(x), 1/float64(n)) == float64(n) {
        return true
    }
    return false
}

