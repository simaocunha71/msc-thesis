
There's no need for the second loop in IsEqualToSumEven function. The numbers are always going to be in ascending order, so you can just increment by 2 each time.
Also, instead of using nested for loops, it's much easier to use one loop that increments by 2, and then add the result of the loop to n. This way, you don't have to check if n is greater than 4, and you can return false immediately if it is.
Here's the updated code:
func IsEqualToSumEven(n int) bool {
    if n % 2 != 0 || n < 8 {
        return false
    }
    for i := 2; i <= n/4; i += 2 {
        if n - i == 2 * i {
            return true
        }
    }
    return false
}