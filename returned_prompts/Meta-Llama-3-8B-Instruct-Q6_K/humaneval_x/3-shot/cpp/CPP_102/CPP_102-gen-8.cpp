    if (x%2==0 && y%2==0)
        return max(x,y);
    else if (x%2==0)
        return x;
    else if (y%2==0)
        return y;
    else
        return -1;
}