    int i;
    for (i=1;i<100;i++)
    {
        if (a%i==0)
        {
            int j;
            for (j=1;j<100;j++)
            {
                if (a%j==0)
                {
                    int k;
                    for (k=1;k<100;k++)
                    {
                        if (a%k==0)
                        {
                            if (i*j*k==a)
                            return true;
                            break;
                        }
                    }
                    break;
                }
            }
            break;
        }
    }
    return false;
}


