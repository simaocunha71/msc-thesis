    if (y%2!=0 && x%2!=0)
    return -1;
    if (y%2==0 && x%2==0)
    return min(x,y);
    else if (y%2==0 && x%2!=0)
    return y;
    else if (y%2!=0 && x%2==0)
    return x;
}

