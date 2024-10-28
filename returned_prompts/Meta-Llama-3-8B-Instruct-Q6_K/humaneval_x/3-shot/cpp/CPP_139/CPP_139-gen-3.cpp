    long long result=1;
    for (int i=n;i>0;i--)
    {
        result *= i;
        for (int j=i-1;j>0;j--)
        {
            result *= j;
        }
    }
    return result;
} // This function seems to be incorrect, it doesn't calculate the brazilian factorial correctly. It seems it calculates the factorial of the factorial.
// A correct function should be:
long long special_factorial(int n){
    long long result=1;
    for(int i=n;i>0;i--){
        result *= fac(i);
    }
    return result;
}
long long fac(int n){
    long long result=1;
    for(int i=n;i>0;i--){
        result *= i;
    }
    return result;
}
// This function correctly calculates the brazilian factorial, it uses a helper function fac() to calculate the factorial. The helper function fac() is used in a loop to calculate the brazilian factorial.