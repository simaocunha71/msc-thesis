    int sum=0;
    for(int i=1;i<=n;i++)
    {
        sum+=i;
    }
    return sum;
}
// or 
int sum_to_n(int n){
    return n*(n+1)/2;
} // this is more efficient and correct
