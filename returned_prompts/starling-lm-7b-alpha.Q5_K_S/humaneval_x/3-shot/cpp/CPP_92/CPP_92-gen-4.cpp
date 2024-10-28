    if (a%1==0 && b%1==0 && c%1==0)
    {
        if ((a==b+c) || (b==a+c) || (c==a+b))
        return true;
    }
    return false;
}





