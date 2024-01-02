
// Return a greatest common divisor of two integers a and b
// >>> GreatestCommonDivisor(3, 5)
// 1
// >>> GreatestCommonDivisor(25, 15)
// 5
func GreatestCommonDivisor(a int,b int) int{
    var result = 0;
    if a > b {
        x = b;
        y = a;
        
    }else{
      x=a;
    	y=b;
    }
    
   for i:=2;i<x/y+1;i++{
            var p,q ;
            if (x%i == 0 && y % i==0) {
                result = int(p + q);
                if result < x {
                    result = int(p)+int(q);
                }
                else {
                    return result;
                }
            }
    }
    
    return result;
}