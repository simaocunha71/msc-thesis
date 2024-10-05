package kata

func Eat(number, need, remaining int) []int {
    if need > remaining {
        number += remaining
        remaining = 0
    } else {
        number += need
        remaining -= need
    }
    return []int{number, remaining}
}