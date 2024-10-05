    int remainder;
    while (b>0)
    {
        remainder=a%b;
        a=b;
        b=remainder;
    }
    return a;
}

