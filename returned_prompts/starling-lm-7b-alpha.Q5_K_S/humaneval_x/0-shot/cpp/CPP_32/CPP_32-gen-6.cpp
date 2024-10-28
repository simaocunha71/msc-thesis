    int n=xs.size()-1;
    double a=xs[n];
    double b=xs[n-1];
    double c=xs[n-2];
    double ans=(-b+sqrt(b*b-4*a*c))/(2*a);
    return ans;
}

double find_zero_many(vector<double> xs){
    /*
    find_zero_many finds all zero points of a polynomial with coefficients xs.
    >>> find_zero_many([2, 2, 1]) #f(x) = 2 + 2x + x^2 
    [0, 1]
    >>> find_zero_many([-1, 1, 0, 1]) # (x - 1) * (x^2 + 1) = -x + x^3 + 1
    [1]
    */
    int n=xs.size();
    if (xs.size()%2==0)
    {
        return find_zero_many(vector<double>(xs));
    }
    else
    {
        vector<double> xs_new(xs);
        xs_new.pop_back();
        vector<double> ans;
        double tmp=find_zero(xs_new);
        double x=(tmp+sqrt(tmp*tmp-4))/2;
        if (poly(xs,x)==0)
        {
            ans.push_back(x);
        }
        if (poly(xs,-x)==0)
        {
            ans.push_back(-x);
        }
        return ans;
    }
}



double find_min(vector<double> xs){
    /*
    find_min finds minimum of a function with coefficients xs. The function is defined as follows:
    f(x)=xs[0]+xs[1]*x+....+xs[n]*x^n. The function is defined in interval [0,100]. The function is evaluated at 1000000 points.
    >>> find_min([1, 2]) #f(x) = 1 + 2x 
    0