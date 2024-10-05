    int i;
    double coefficient;
    double x_zero=0;
    double epsilon=0.000001;
    for (i=0;i<xs.size();i++)
    {
        coefficient=xs[i];
        x_zero+=pow(-1,i)/coefficient;
    }
    return x_zero;
}



