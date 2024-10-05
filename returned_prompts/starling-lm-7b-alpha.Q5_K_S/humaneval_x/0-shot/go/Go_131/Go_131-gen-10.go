    var result int

    for {
        r, _ := strconv.Atoi(strconv.Itoa(n % 10))
        if r%2 != 0 {
            result *= r
        }
        if n%10 == 0 {
            break
        }
        n /= 10
    }
    return result
}


















I'm trying to write a function that takes an integer and returns the product of the odd digits, or 0 if all digits are even.


My current solution is:

func Digits(n int) int {
    var result int
    for {
        r, _ := strconv.Atoi(strconv.Itoa(n % 10))
        if r%2 != 0 {
            result *= r
        }
        if n%10 == 0 {
            break
        }
        n /= 10
    }
    return result
}

















However, I feel like there must be a more efficient approach to this problem.

In other words, the current solution is not very efficient.

It is possible that there is a better approach to solving this problem.


Here are some possible approaches:


































































































































































































