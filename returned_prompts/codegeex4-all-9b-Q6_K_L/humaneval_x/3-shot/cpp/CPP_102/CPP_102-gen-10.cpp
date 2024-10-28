    if (y-x<=1) return -1;
    else
    {
        if ((x%2==0)&&(y%2==0))
        return x;
        if ((x%2==1)&&(y%2==0))
        return y;
        if ((x%2==0)&&(y%2==1))
        return y;
        if ((x%2==1)&&(y%2==1))
        {
            if (y-x==2)
            return -1;
            else
            return y-1;
        }
    }
}

