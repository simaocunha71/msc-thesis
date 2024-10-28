    float p,s;
    p=(a+b+c)/2;
    s=sqrt(p*(p-a)*(p-b)*(p-c));
    if (s<0)
    return -1;
    else
    return round(s*a*b*c/4);
}



