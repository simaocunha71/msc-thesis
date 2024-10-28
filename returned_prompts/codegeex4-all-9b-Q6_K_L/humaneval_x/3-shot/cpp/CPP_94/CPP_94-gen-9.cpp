    int max=0;
    for (int i=0;i<lst.size();i++)
    {
        int num=lst[i];
        bool is_prime=true;
        for (int j=2;j<num;j++)
        if (num%j==0)
        {
            is_prime=false;
            break;
        }
        if (is_prime)
        if (num>max)
        max=num;
    }
    int sum=0;
