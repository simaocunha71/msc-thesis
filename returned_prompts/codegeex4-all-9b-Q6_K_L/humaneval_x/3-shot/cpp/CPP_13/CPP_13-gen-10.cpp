    int r=a%b;
    if (r==0)
    return b;
    else
    return greatest_common_divisor(b,r);
}

