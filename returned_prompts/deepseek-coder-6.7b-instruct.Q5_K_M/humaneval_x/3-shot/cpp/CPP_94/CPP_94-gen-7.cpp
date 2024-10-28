    int max_prime=0;
    for(int i=0;i<lst.size();i++)
    {
        int num=lst[i];
        if(num>max_prime)
        {
            bool prime=true;
            for(int j=2;j*j<=num;j++)
            {
                if(num%j==0)
                {
                    prime=false;
                    break;
                }
            }
            if(prime)
            {
                max_prime=num;
            }
        }
    }
    int sum=0;
    while(max_prime>0)
    {
        sum+=max_prime%10;
        max_prime/=10;
    }
    return sum;
}


