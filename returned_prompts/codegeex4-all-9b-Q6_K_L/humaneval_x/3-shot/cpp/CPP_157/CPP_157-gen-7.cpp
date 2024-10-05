    float max;
    if (a>b && a>c)
    max=a;
    if (b>a && b>c)
    max=b;
    if (c>a && c>b)
    max=c;

    if (pow(max,2)==pow(a,2)+pow(b,2) || pow(max,2)==pow(a,2)+pow(c,2) || pow(max,2)==pow(b,2)+pow(c,2))
    return true;

    return false;
}

