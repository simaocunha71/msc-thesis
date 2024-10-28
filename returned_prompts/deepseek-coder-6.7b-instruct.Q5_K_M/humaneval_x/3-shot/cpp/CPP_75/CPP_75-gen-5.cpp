    int i,j,fact=0;
    for(i=2;i<=a;i++)
    {
        if(a%i==0)
        {
            for(j=2;j<=i;j++)
            {
                if(i%j==0)
                {
                    break;
                }
            }
            if(i==j)
            {
                fact++;
            }
        }
    }
    if(fact==3)
    {
        return true;
    }
    else
    {
        return false;
    }
}

