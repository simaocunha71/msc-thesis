    double x=0;
    double fx;
    int i;
    for (i=0;i<1000000;i++)
    {
        x+=poly(xs,x)/poly(vector<double>{xs[1]+xs[0],xs[2]+2*xs[0],xs[3]+3*xs[0],xs[4]+4*xs[0]},x)/10000;
        fx=poly(xs,x);
        if (fabs(fx)<0.000000001){
        return x;
        }
    }
    return x;
}



