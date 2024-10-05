    int b;
    for (b=1;b<pow(a,1.0/3)+1;b++)
    {
        if (b*b*b==a)
        return true;
    }
    return false;
}

