func RightAngleTriangle(a, b, c int) bool {
    sides := []int{a, b, c}
    sort.Ints(sides)
    return sides[0]*sides[0] + sides[1]*sides[1] == sides[2]*sides[2]
}