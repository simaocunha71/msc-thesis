    if (n<2)
    return false;
    for (long long i=2;i*i<=n;i++)
    if (n%i==0)
    return false;
    return true;
}
bool is_prime(int n){
    if (n<2)
    return false;
    for (int i=2;i*i<=n;i++)
    if (n%i==0)
    return false;
    return true;
} // Note: I added an integer version of the function as well. The logic is same, but the condition i*i<=n is used to avoid unnecessary iterations. 
// For example, if n is 10, then we don't need to check divisibility with 8, 9 because 8 and 9 are greater than square root of 10. 

