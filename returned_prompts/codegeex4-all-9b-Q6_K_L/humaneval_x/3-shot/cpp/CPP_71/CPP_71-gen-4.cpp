    if (a+b<=c)
        return -1;
    if (a+c<=b)
        return -1;
    if (b+c<=a)
        return -1;
    float p=(a+b+c)/2;
    return round(sqrt(p*(p-a)*(p-b)*(p-c))*100)/100;
}

