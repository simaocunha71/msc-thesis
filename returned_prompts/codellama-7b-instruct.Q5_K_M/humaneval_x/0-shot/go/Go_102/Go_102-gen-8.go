
// 1.
// x, y > 0
// x, y 是两个正整数，如果 y 不大于 x，则返回 -1，否则循环查找 2 的幂。
func ChooseNum(x, y int) int {
    if y <= x {
        return -1
    }
    var z int
    for z = 1; z <= y; z <<= 1 {
        if z >= x {
            return z
        }
    }
    return -1
}

B:

// 2.
// x, y > 0
// x, y 是两个正整数，如果 y 不大于 x，则返回 -1，否则循环查找 2 的幂。
func ChooseNum(x, y int) int {
    if y <= x {
        return -1
    }
    var z int
    for z = 1; z <= y; z <<= 1 {
        if z >= x && z%2 == 0 {
            return z
        }
    }
    return -1
}

C:

// 3.
// x, y > 0
// x, y 是两个正整数，如果 y 不大于 x，则返回 -1，否则循环查找 2 的幂。
func ChooseNum(x, y int) int {
    if y <= x {
        return -1
    }
    var z int
    for z = 1; z <= y; z <<= 1 {
        if z >= x && z%2 == 0 {
            return z
        }
    }
    return -1
}

D:

// 4.
// x, y > 0
// x, y 是两个正整数，如果 y 不大于 x，则返回 -1，否则循环查找 2 的幂。
func ChooseNum(