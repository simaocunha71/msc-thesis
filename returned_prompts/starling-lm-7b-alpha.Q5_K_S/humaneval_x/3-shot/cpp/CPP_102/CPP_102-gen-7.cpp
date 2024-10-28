    if (x%2!=0)
    {
        if (y%2!=0)
        {
            if (y>x)
            return x;
            else
            return -1;
        }
        else
        {
            return x;
        }
    }
    else
    {
        if (y%2!=0)
        {
            return y-1;
        }
        else
        {
            if (y>x)
            return y;
            else
            return -1;
        }
    }
}



