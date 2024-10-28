    sides := []int{a, b, c}
    for i := 0; i < 3; i++ {
        for j := i + 1; j < 3; j++ {
            if sides[i]*sides[i] + sides[j]*sides[j] == sides[3-i-1]*sides[3-i-1] {
                return true
            }
        }
    }
    return false
}