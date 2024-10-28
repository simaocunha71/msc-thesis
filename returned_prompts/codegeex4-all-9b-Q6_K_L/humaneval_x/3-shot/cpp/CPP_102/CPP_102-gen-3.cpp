    if (x%2==0 && y%2==0 && x<=y)
    return y;
    if (x%2==0 && y%2==0 && x>=y)
    return x;
    if (x%2!=0 && y%2==0 && x<=y)
    return y;
    if (x%2!=0 && y%2==0 && x>=y)
    return x;
    if (x%2==0 && y%2!=0 && x<=y)
    return y-1;
    if (x%2==0 && y%2!=0 && x>=y)
    return x;
    if (x%2!=0 && y%2!=0 && x<=y)
    return y-1;
    if (x%2!=0 && y%2!=0 && x>=y)
    return x-1;
    return -1;
}

