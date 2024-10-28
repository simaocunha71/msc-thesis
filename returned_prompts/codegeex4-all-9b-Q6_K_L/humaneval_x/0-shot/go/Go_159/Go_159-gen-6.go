// There are 4 variables to consider:
// number - the number of carrots that you have Eaten.
// need - the number of carrots that you need to Eat.
// remaining - the number of remaining carrots thet exist in stock
// total - the total number of Eaten carrots after your meals.

// If the need is greater than the remaining, then the total is the sum of the number and the remaining.
// If the need is less than or equal to the remaining, then the total is the sum of the number and the need.
// If the need is equal to the remaining, then the number is 0 and the total is the sum of the number and the need.
// If the need is equal to 0, then the number is 0 and the total is 0.
// If the need is equal to the number, then the remaining is 0 and the total is the sum of the number and the need.
func Eat(number, need, remaining int) []int {
    if need > remaining {
        return []int{number + remaining, 0}
    } else if need <= remaining {
        return []int{number + need, remaining - need}
    } else if need == remaining {
        return []int{number, 0}
    } else if need == 0 {
        return []int{0, 0}
    } else if need == number {
        return []int{number, 0}
    } else {
        return []int{0, 0}
    }
}