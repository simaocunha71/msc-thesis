
You are calculating the wrong numbers.
The number of n digit numbers that start with 1 is 9*(10^(n-2)) - 1
The number of n digit numbers that end with 1 is 9*(10^(n-2)) - 1
The total number of n digit numbers that start or end with 1 is 9*(10^(n-2)) - 1 + 9*(10^(n-2)) - 1 = 18*(10^(n-2)) - 2
So your function should be:
func StartsOneEnds(n int) int {
    if n==1{
        return 2
    }
    if n==2{
        return 5
    }
    return int(18*math.Pow(10,n-2)) - 2
}