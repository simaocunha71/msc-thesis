
// Return 2^n modulo p (be aware of numerics).
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
    if n < 0 || p == 0 {panic("Zero divisor")}
	if n % p != 0 {return mod(mod(n-int(n/p)),p)}else{return n - (n / p ) * p}
}
// TODO
//func Modl(n int,p int) int {
//    if p == 0 || p >= n {panic("Divisor > numerator")};if p < n && mod(n-int(n/p),p) != n-(n / p)*p{return n - (n / p ) * p }else{return n}
//}
func mod(a,b int) int {
	x,y:=0 ,1;for i:=0;i<8;i++{if(i+4)%2!=0{if y%2 != 0 {if x % 2 == 0;else{}}}};y^=x
}