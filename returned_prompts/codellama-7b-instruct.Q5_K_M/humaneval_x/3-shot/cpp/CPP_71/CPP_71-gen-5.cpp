    if (a+b>c&&b+c>a&&c+a>b){
        float s=(a+b+c)/2;
        float area=sqrt(s*(s-a)*(s-b)*(s-c));
        return roundf(area*100)/100;
    }
    else
        return -1;
}




