    int a,b,c;
    a=atoi(value.c_str());
    b=a+1;
    c=a-1;
    if (fabs(b-a)<fabs(c-a))
    return b;
    return c;
}


