
// Your task is to write a function that returns true if a number x is a simple
// power of n and false in other cases.
// x is a simple power of n if n**int=x
// For example:
// IsSimplePower(1, 4) => true
// IsSimplePower(2, 2) => true
// IsSimplePower(8, 2) => true
// IsSimplePower(3, 2) => false
// IsSimplePower(3, 1) => false
// IsSimplePower(5, 3) => false
func IsSimplePower(x int,n int) bool {
	if x == 0 || n == 0{
		return true
	}
	var power = make([]int,len(n)+1);
	pow := 1;
	for i:=0;i<len(n);i++{
		pow *= n[i];
		power[i] = pow % x;
		if power[i] == 0 {return false;}
	}
	if x%power[len(x)] == 0 {
		return true;
	}else{
		return false;
	}
}