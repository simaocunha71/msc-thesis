    double a=0;
    double b=1;
    double fa=poly(xs,a);
    double fb=poly(xs,b);
    double c;
    double fc;
    while (fabs(fa)>0.001){
        c=(a*fb-b*fa)/(fb-fa);
        fc=poly(xs,c);
        if (fc==0) return c;
        if (fa*fc<0) {b=c;fb=fc;}
        else {a=c;fa=fc;}
    }
    return a;
}

