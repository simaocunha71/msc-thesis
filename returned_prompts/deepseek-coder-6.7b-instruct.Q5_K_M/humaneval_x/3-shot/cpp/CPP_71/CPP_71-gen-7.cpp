    if(a+b<=c || b+c<=a || c+a<=b)
        return -1;
    float s=(a+b+c)/2;
    float area=sqrt(s*(s-a)*(s-b)*(s-c));
    return round(area*100)/100;
}

