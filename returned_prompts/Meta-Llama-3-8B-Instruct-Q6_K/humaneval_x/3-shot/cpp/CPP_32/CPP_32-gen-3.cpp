    double x=0;
    double sum=poly(xs,x);
    double eps=0.00001;
    while (abs(sum)>eps)
    {
        x=x- sum/poly(vector<double>(xs.begin(),xs.end()),x);
    }
    return x;
}