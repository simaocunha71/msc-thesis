    len := len(s)
    if len <= 1 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(len))); i++ {
        if len%i == 0 {
            return false
        }
    }
    return true
}  // Thanks to @Sergio for pointing out a mistake in my previous version. I had a bug where I was checking if the length was divisible by 1, which is always true. This version of the function correctly checks if the length is divisible by any number from 2 to the square root of the length. If it is, then it's not a prime number and the function returns false. If it's not divisible by any of these numbers, then it is a prime number and the function returns true.