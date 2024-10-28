    float a1,b1,c1;

    a1=pow(a,2);
    b1=pow(b,2);
    c1=pow(c,2);

    if (a1+b1==c1 || a1+c1==b1 || b1+c1==a1)
    return true;
    else
    return false;
}

