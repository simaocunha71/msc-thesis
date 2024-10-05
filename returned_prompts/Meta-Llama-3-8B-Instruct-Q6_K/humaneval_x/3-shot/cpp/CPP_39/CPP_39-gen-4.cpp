    int a=0, b=1;
    int i;
    for (i=0;i<n;i++)
    {
        int temp=a+a+b;
        if (is_prime(temp))
        {
            return temp;
        }
        a=b;
        b=temp;
    }
    return 0;
}
bool is_prime(int num){
    if(num<2) return false;
    for(int i=2;i*i<=num;i++)
    {
        if(num%i==0)
        return false;
    }
    return true;
}
// You can also use a function like this:
// bool is_prime(int num){
//     if(num<2) return false;
//     for(int i=2,sqrt_num=sqrt(num);i<=sqrt_num;i++)
//     {
//         if(num%i==0)
//         return false;
//     }
//     return true;
// } // This version is slightly more efficient.