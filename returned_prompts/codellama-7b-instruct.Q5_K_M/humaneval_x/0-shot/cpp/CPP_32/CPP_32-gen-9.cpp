    int i;
    double a = xs[0];
    if (xs.size() % 2 == 1 || a == 0)
    {
        printf("Error! find_zero only takes even number of coefficients and largest non zero coefficient as it guarantees a solution.");
        return -1;
    }

    // find the highest power of x
    int n = 1;
    for (i = 1; i < xs.size(); i++)
    {
        if (xs[i] != 0)
        {
            n = i;
        }
    }

    // find the x-intercept
    double x0 = -a / xs[n];
    return x0;
}

// find_max
double find_max(vector<double> xs){
    /*
    find_max finds the max value of the polynomial with coefficients xs. 
    >>> find_max([1, 2, 3, 4]) 
    4 
    */
    int i;
    double max = xs[0];
    for (i = 1; i < xs.size(); i++)
    {
        if (xs[i] > max)
        {
            max = xs[i];
        }
    }
    return max;
}

// find_min
double find_min(vector<double> xs){
    /*
    find_min finds the min value of the polynomial with coefficients xs. 
    >>> find_min([1, 2, 3, 4]) 
    1 
    */
    int i;
    double min = xs[0];
    for (i = 1; i < xs.size(); i++)
    {
        if (xs[i] < min)
        {
            min = xs[i];
        }
    }
    return min;
}

int main(){
    vector<double> xs = {1, 2, 3, 4};
    printf("max(xs) = %f\n", find_max(xs));
    printf("min(xs) = %f\n", find_min(xs));
    vector<double> xs2 = {-6, 