    float temp;
    if(a>b && a>c){
        temp=a;
        a=c;
        c=temp;
    }
    else if(b>a && b>c){
        temp=b;
        b=c;
        c=temp;
    }

    if(pow(c,2)==(pow(a,2)+pow(b,2)))
    return true;
    else 
    return false;
}


