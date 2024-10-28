    c := int(math.Pow(float64(int(math.Ceil(math.Sqrt(float64(a))))), 3))
    return c == a
}  // or 
func Iscube(a int) bool {
    c := int(math.Pow(float64(math.Ceil(math.Sqrt(float64(float64(a))))), 3))
    return c == a
}  // or 
func Iscube(a int) bool {
    i := 0
    for c := int(math.Pow(float64(i), 3)); c < a; i++ {
        c = int(math.Pow(float64(i), 3))
    }
    return c == a
}  // or 
func Iscube(a int) bool {
    i := 0
    c := int(math.Pow(float64(i), 3))
    for ; c < a; i++ {
        c = int(math.Pow(float64(i), 3))
    }
    return c == a
}  // or 
func Iscube(a int) bool {
    i := 0
    for c := int(math.Pow(float64(i), 3)); c <= a; i++ {
        if c == a {
            return true
        }
        i++
    }
    return false
}  // or 
func Iscube(a int) bool {
    i := 0
    for {
        c := int(math.Pow(float64(i), 3))
        if c > a {
            return false
        }
        if c == a {
            return true
        }
        i++
    }
}  // or 
func Iscube(a int) bool {
    i := 0
    for c := int(math.Pow(float64(i), 3)); ; i++ {
        if c > a {
            return false
        }
        if c == a {
            return true
        }
    }
}  // or 
func Iscube(a int) bool {
    i := 0
    for c := int(math.Pow(float64(i), 3)); ; i++ {
        if c > a {
            return false
        }
        if c == a {
            return true
        }
    }
}  // or 
func Iscube(a int) bool {
    i := 0
    for {
        c := int(math.Pow(float64(i), 3))
        if c > a {
            return false
        }
        if c == a {
            return true
        }
        i++
    }
}  //