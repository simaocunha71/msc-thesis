    double res=pow(n,log(x)/log(n));
    return res==x;
}
//or
bool is_simple_power(int x,int n){
    double res=pow(n,floor(log(x)/log(n)));
    return res==x;
}  //Note: pow and log are not defined for all values
//Note: These functions may not work correctly for negative numbers or very large numbers

//You can use integer math for integer values of x and n
bool is_simple_power(int x,int n){
    int exp=floor(log(x)/log(n));
    return pow(n,exp)==x;
}
//Note: pow and log are not defined for all values
//Note: These functions may not work correctly for negative numbers or very large numbers

