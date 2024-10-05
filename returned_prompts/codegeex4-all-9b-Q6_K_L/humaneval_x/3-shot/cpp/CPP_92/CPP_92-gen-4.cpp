    if (a+b==c && a==int(a) && b==int(b) && c==int(c))
    return true;
    if (a+c==b && a==int(a) && b==int(b) && c==int(c))
    return true;
    if (b+c==a && a==int(a) && b==int(b) && c==int(c))
    return true;
    return false;
}

