    if (a+b>c && b+c>a && a+c>b)
    return (float)((a+b+c)/2)*sqrt((a+b+c)/2-(a+b-c)*(a+b-c)/(a+b+c))/100;
    else 
    return -1;
}

