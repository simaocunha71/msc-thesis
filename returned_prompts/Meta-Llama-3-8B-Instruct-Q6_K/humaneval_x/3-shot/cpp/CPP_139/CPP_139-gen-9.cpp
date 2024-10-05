    long long result=1;
    for (int i=n; i>0; i--)
    {
        result*=i;
    }
    return result;
} // or use the gamma function if you want to avoid overflow for large n
#include<cmath>
long long special_factorial(int n){
    return tgamma(n+1);
} // remember that gamma(0) is not defined, so you should add 1 to n
}  // The function should return a long long, not a double. So we use long long instead of double. And the result of the gamma function is not a long long, so we should return it as long long. 
}  // The function should return a long long, not a double. So we use long long instead of double. And the result of the gamma function is not a long long, so we should return it as long long. 

