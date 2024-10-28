    float p,s,area;
    p=(a+b+c)/2;
    s=sqrt(p*(p-a)*(p-b)*(p-c));
    area=s*p;
    return round(area*100)/100;
}


