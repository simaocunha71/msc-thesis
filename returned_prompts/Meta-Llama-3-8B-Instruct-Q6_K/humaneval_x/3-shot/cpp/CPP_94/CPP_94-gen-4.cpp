    int max_prime=0;
    int sum=0;
    for (int i=0;i<lst.size();i++)
    {
        bool is_prime=true;
        if (lst[i]<2)
        {
            continue;
        }
        for (int j=2;j<=sqrt(lst[i]);j++)
        {
            if (lst[i]%j==0)
            {
                is_prime=false;
                break;
            }
        }
        if (is_prime)
        {
            if (lst[i]>max_prime)
            {
                max_prime=lst[i];
            }
        }
    }
    if (max_prime!=0)
    {
        sum=0;
        while (max_prime>0)
        {
            sum+=(max_prime%10);
            max_prime/=10;
        }
        return sum;
    }
    else
    {
        return 0;
    }
} // end of function skjkasdkd


