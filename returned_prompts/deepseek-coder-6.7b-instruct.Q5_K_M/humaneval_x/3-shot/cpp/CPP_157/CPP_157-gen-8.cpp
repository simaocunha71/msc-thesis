    float temp;
    if(a>b && a>c) {temp=a; a=c; c=temp;}
    if(b>a && b>c) {temp=b; b=c; c=temp;}
    return (c*c==(a*a+b*b));
}

