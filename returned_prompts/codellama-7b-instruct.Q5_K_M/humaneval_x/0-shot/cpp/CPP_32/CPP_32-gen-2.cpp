    int n=xs.size();
    if (n%2!=0)
    {
        printf("Warning: odd number of coefficients. find_zero returns only one solution, even if there are many.\n");
        printf("find_zero([1, 2]) returns x = -0.5 \n");
        printf("find_zero([-6, 11, -6, 1]) returns x = 1.0\n");
    }
    else if (n==2)
    {
        return -xs[0]/xs[1];
    }
    else if (xs[n-2]==0)
    {
        printf("Warning: non zero coefficient must be the largest non zero coefficient\n");
        printf("find_zero([1, 2]) returns x = -0.5 \n");
        printf("find_zero([-6, 11, -6, 1]) returns x = 1.0\n");
    }
    else
    {
        int i;
        double a = xs[n-2];
        double b = xs[n-1];
        double c = 0;
        for (i=0;i<n-2;i++)
        {
            c+=xs[i]*pow(a,i);
        }
        double d = b*pow(a,n-2)-c;
        double e = -pow(a,n-1);
        double x1 = (d+sqrt(d*d-4*c*e))/(2*c);
        double x2 = (d-sqrt(d*d-4*c*e))/(2*c);
        return x2;
    }
}

double find_zero_by_newton(vector<double> xs, double x){
    /*
    xs are coefficients of a polynomial. find_zero_by_newton find x such that poly(x) = 0. find_zero_by_newton returns only only zero point, even if there are many. 
    Moreover, find_zero_by_newton only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero_