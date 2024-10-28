    if (b==0)
    return a;
    else
    return greatest_common_divisor(b,a%b);
}
//or
#include<math.h>
int greatest_common_divisor(int a, int b){
    return gcd(a,b);
}
#include<gmp.h>
int greatest_common_divisor(int a, int b){
    return gcd_ui(a,b);
}
//or
#include<gmpxx.h>
int greatest_common_divisor(int a, int b){
    return __gcd(a,b);
}

