    int i;
    for (i=0;i<xs.size();i++){
        if (xs[i]!=0) break;
    }
    if (i==xs.size()){
        cout<<"No solution"<<endl;
        return 0;
    }
    if ((i%2)!=0){
        cout<<"No solution"<<endl;
        return 0;
    }
    double x=xs[i];
    for (i=i+1;i<xs.size();i++){
        x=-xs[i]/xs[i-1];
    }
    return x;
}

double find_min(vector<double> xs){
    /*
    xs are coefficients of a polynomial. find_min finds the minimum of the polynomial. find_min returns only only minimum point, even if there are many. 
    Moreover, find_min only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> find_min([1, 2, 3, 4]) # (x - 1) * (x - 2) * (x - 3) * (x - 4) = 1 + 2x + 3x^2 + 4x^3
    1
    >>> find_min([1, 2, 3, 4, 5]) # (x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5) = 1 + 2x + 3x^2 + 4x^3 + 5x^4
    1
    */
    int i;
    for (i=0;i<xs.size();i++){
        if (xs[i]!=0) break;
    }
    if (i==xs.size()){
        cout<<"No solution"<<endl;
        return 0;
    }
    if ((i%2)!=0){
        cout<<"No solution"<<endl;
        return 0;
    }
    double x=xs[i];
    for (i=i+1;i<xs.size();i++){
        x