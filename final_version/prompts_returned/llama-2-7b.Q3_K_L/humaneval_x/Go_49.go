
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
    var s uint64 = ^uint64(0)
	for t := uint64(0); t < uint64(n+1) && s != 0;t++{
		if n%t == 0{
			s--
		} else {
			s += 1
		}
		if s > p {
			return int((s-p)&(1<<64 - 1)) + 1
		}
    }
	panic("Modp: " + strconv.Itoa(int(n)))
}