    float max_side;
    if (a>b && a>c)
    max_side=a;
    else
    if (b>a && b>c)
    max_side=b;
    else
    max_side=c;

    if (max_side==a)
    return (pow(max_side,2)==pow(b,2)+pow(c,2));
    else
    if (max_side==b)
    return (pow(max_side,2)==pow(a,2)+pow(c,2));
    else
    return (pow(max_side,2)==pow(a,2)+pow(b,2));
}

