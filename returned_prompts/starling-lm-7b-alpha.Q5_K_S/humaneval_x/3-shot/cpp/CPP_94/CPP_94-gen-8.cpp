    int i,j;
    int prime_max=-1;
    int sum=0;
    for (i=0;i<lst.size();i++)
    {
        if (prime_max<lst[i])
        {
        prime_max=lst[i];
        while (prime_max>1){
        j=2;
        while (j<prime_max){
        if (prime_max%j==0)
        break;
        j+=1;
        }
        if (j==prime_max)
        break;
        else
        prime_max-=1;
        }
        }
    }
    while (prime_max>1){
    j=2;
    while (j<prime_max){
    if (prime_max%j==0)
    break;
    j+=1;
    }
    if (j==prime_max)
    break;
    else
    prime_max-=1;
    }
    while (prime_max>0){
    sum+=prime_max%10;
    prime_max/=10;
    }
    return sum;
}


