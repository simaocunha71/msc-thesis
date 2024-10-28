    double a=1,b=2;
    double fa=poly(xs,a);
    double fb=poly(xs,b);
    while (abs(a-b)>0.00001){
        double c=(a+fa*(b-a)/(fb-fa));
        double fc=poly(xs,c);
        if (fc==0) return c;
        if (fc*fb<0){
            a=b;
            fa=fb;
            b=c;
            fb=fc;
        }
        else {
            fa=fc;
            a=c;
        }
    }
    return b;
}

