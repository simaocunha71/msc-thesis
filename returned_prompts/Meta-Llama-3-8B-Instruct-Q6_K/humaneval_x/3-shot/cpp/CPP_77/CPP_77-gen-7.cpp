    int i;
    for (i=0;i<=sqrt(a);i++)
    {
        if (pow(i,3)==a)
        {
            return true;
        }
    }
    return false;
}