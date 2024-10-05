    float p=(a+b+c)/2;
    if (a+b>c && b+c>a && c+a>b)
        return sqrt(p*(p-a)*(p-b)*(p-c));
    else
        return -1;
}



