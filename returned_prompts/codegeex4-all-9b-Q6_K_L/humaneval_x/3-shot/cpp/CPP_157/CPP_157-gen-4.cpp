    float a2=pow(a,2);
    float b2=pow(b,2);
    float c2=pow(c,2);
    if (a2+b2==c2)
    return true;
    if (a2+c2==b2)
    return true;
    if (b2+c2==a2)
    return true;
    return false;
}

