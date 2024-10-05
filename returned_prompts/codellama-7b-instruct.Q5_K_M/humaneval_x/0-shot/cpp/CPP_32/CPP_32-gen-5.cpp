    if(xs.size()%2 == 1)
    {
        printf("error: find_zero needs a list with even number of coefficients");
        return 0;
    }
    int i;
    double x_0 = xs[xs.size()-1];
    for (i=xs.size()-2;i>=0;i-=2)
    {
        x_0 = -xs[i]/xs[i-1] + x_0;
    }
    return x_0;
}

int main(){
    vector<double> xs;
    xs.push_back(1);
    xs.push_back(2);
    printf("%f",find_zero(xs));
}