    int i,div;
    for (i=2;i<sqrt(a)+1;i++)
    {
        div=a/i;
        if (div*i==a && i!=div)
        return false;
    }
    return true;
}

