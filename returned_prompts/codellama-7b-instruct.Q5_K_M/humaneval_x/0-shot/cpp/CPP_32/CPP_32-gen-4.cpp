    if (xs.size()==1) return 0;
    if (xs.size()%2!=0) return 0;
    double max = 0;
    int imax = 0;
    for (int i=1;i<xs.size();i++){
        if (abs(xs[i])>max){
            max = abs(xs[i]);
            imax = i;
        }
    }
    double a = xs[imax];
    double b = xs[imax-1];
    if (a==0) return 0;
    return -b/a;
}


double find_min(vector<double> xs){
    /*
    xs is a list of coefficients of a polynomial. find_min finds minimum of the polynomial.
    >>> find_min([1, 2, 3]) #f(x) = 1 + 2x + 3x^2 
    1.0 
    >>> find_min([-1, 1]) #f(x) = -1 + x 
    0.0 
    >>> find_min([1, -1]) #f(x) = 1 - x 
    1.0 
    */
    if (xs.size()==1) return 0;
    double min = 0;
    int imin = 0;
    for (int i=1;i<xs.size();i++){
        if (xs[i]<min){
            min = xs[i];
            imin = i;
        }
    }
    return -min/xs[imin];
}


int main(){
    vector<double> xs = {1, 2, 3};
    printf("find_zero(%d) = %f\n", xs.size(), find_zero(xs));
    xs = {1, 2, 3, 4};
    printf("find_zero(%d) = %f\n", xs.size(), find_zero(xs));
    xs = {1, 2, 3, 4, 5};
    printf("find_zero(%d) = %f\n", xs.size(), find_zero(