    if (a+b>c && b+c>a && c+a>b)
    {
        float s=(a+b+c)/2;
        return sqrt(s*(s-a)*(s-b)*(s-c));
    }
    else
    return -1;
}

