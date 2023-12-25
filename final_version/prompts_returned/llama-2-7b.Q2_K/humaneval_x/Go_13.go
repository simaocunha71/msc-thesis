
// Return a greatest common divisor of two integers a and b
// >>> GreatestCommonDivisor(3, 5)
// 1
// >>> GreatestCommonDivisor(25, 15)
// 5
func GreatestCommonDivisor(a int,b int) int{
    var n, d int
    if a == b {
       return a
    } else {
      for i := 3; ;i += 4 {
        if (i*2+1)/i > a && (i*2+1)/i > b {
           // this is the most efficient way to find GCD
           n = int(float64(b)) * (float64(a) / float64((i-1)))
        } else if i == 3 || i >= a {
          d = GreatestCommonDivisor(int(n), b - a)
        } else if (i + 2) % n != 0 && i > 1 {
           d = int(a / n)
       } else {
         return a
       }
    // return (a/d) + (b/d)
      for ;i++; i <= b;i++ { if (i < int(d)) break }
        if d >= b-i && d != a {
          d += GreatestCommonDivisor(int(n), int(d)-1)
       // return ((a/d)+((b/d)-1))
   } else break
   }
    n = 0
   for ;; { if (i < int(d)) break }
      d += GreatestCommonDivisor(int(n), i-1)
   // return ((a/(d+1))+(b/((d+1)-1)))
}
