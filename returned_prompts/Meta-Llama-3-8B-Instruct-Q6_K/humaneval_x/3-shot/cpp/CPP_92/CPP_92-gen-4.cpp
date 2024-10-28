    if (a-int(a)!=0 || b-int(b)!=0 || c-int(c)!=0)
    return false;
    if (a==(b+c) || a==(c+b) || a==(b+c))
    return true;
    return false;
}