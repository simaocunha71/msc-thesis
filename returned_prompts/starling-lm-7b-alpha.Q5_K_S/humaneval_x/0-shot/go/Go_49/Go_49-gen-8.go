
if n >= p {
    return Modp(n%p,p)
}
if n < 0 {
    return Modp(n+p,p)
}
return n
}

// Return the sum of all numbers from a to b modulo p
// >>> Sum(2,5,3)
// 9
// >>> Sum(2,10,3)
// 51
// >>> Sum(2,0,3)
// 1
// >>> Sum(2,-1,3)
// 2
func Sum(a, b int, p int) int {
    return Modp(Modp(a,p)+Modp(b,p),p)
}

// Return the product of all numbers from a to b modulo p
// >>> Product(2,5,3)
// 30
// >>> Product(2,10,3)
// 165
// >>> Product(2,0,3)
// 1
// >>> Product(2,-1,3)
// 2
func Product(a, b int, p int) int {
    if a > b {
        return 0
    }
    return Modp(Modp(a,p)*Modp(b,p),p)
}
























































































































































































































