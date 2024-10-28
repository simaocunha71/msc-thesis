
    return int(math.Pow(2, float64(n)))%p

}


A: 

// Return 2^n modulo p  (be aware of numerics).
// 
// >>> Modp(3, 5)
// 3
// >>> Modp(1101, 101)
// 2
// >>> Modp(0, 101)
// 1
// >>> Modp(3, 11)
// 8
// >>> Modp(100, 101)
// 1
func Modp(n int,p int) int {
    if n == 0 {
        return 1 % p
    }
    result := 1
    base := 2
    for n > 0 {
        if n & 1 != 0 {
            result = (result * base) % p
        }
        base = (base * base) % p
        n >>= 1
    }
    if result < 0 {
        result += p
    }
    return result
}


A: 

// Return 2^n modulo p  (be aware of numerics).
// 
// >>> Modp(3, 5)
// 3
// >>> Modp(1101, 101)
// 2
// >>> Modp(0, 101)
// 1
// >>> Modp(3, 11)
// 8
// >>> Modp(100, 101)
// 1
func Modp(n int,p int) int {
    res := 1
    for n > 0 {
        if n % 2 == 1 {
            res = (res * 2) % p
        }
        n = n / 2
        if n > 0 {
            res = (res * res) % p
        }
    }
    return res
}


A: 

// Return 2^n modulo p  (be aware of numerics).
// 
// >>> Modp(3, 5)
// 3
