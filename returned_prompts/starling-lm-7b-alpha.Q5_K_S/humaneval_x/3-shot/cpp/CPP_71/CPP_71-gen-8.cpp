    float p=(a+b+c)/2;
    if (a+b>c&&a+c>b&&b+c>a)
    return sqrt(p*(p-a)*(p-b)*(p-c));
    else
    return -1;
}



