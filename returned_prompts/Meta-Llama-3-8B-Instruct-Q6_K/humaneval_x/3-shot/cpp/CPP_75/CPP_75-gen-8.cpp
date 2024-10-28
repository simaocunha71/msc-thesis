    for (int i=2;i<=sqrt(a);i++)
    {
        if (a%i==0)
        {
            int j=i;
            while (a%i==0)
            {
                a=a/i;
            }
            int count=0;
            while (j>1)
            {
                if (j%2==0 || j%3==0)
                {
                    j=j/2;
                    while (j%2==0) j=j/2;
                    j=j/3;
                    while (j%3==0) j=j/3;
                }
                else
                {
                    count++;
                    j--;
                }
            }
            if (count<3)
            {
                return true;
            }
        }
    }
    return false;
}