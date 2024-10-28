    if (a+b>c && b+c>a && c+a>b)
    return roundf((float)((a+b+c)*sqrt(1/2.0))*100)/100;
    else
    return -1;
}


