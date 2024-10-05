    int i,j,k;
    int b;
    for (i=2;i<=a/2;i++)
    {
        b=a%i;
        if (b==0)
        {
            return false;
        }
    }
    return true;
}


