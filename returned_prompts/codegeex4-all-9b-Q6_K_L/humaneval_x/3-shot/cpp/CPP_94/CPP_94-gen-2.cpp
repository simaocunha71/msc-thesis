    int i,j;
    if (num<=1)
        return false;
    else
    {
        for (i=2;i<=sqrt(num);i++)
        {
            if (num%i==0)
                return false;
        }
        return true;
    }
}

