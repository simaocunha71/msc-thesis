
double x0;
double x1;
double x2;
int n;

n=xs.size();

x0=xs[n-2];
x1=xs[n-1];
x2=xs[n-0];


if (x0 == 0)
{
    return -x1/(3*x2);
}
else 
{
    return -x0/(3*x1) + (-x0*x0*x0+x1*x1*x1-3*x0*x1*x2)/(2*x1*x1*x2);
}
}





