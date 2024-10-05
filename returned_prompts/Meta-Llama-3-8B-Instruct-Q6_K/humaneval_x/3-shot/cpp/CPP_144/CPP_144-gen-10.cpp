    int numerator_x,denominator_x,numerator_n,denominator_n;
    int gcd;
    string result;
    numerator_x=atoi(strtok(x,"/"));
    denominator_x=atoi(strtok(NULL,"/"));
    numerator_n=atoi(strtok(n,"/"));
    denominator_n=atoi(strtok(NULL,"/"));
    gcd=gcd_function(numerator_x*denominator_n,denominator_x*numerator_n);
    result=to_string(numerator_x*denominator_n/gcd)+"/"+to_string(denominator_x*numerator_n/gcd);
    return ( numerator_x*denominator_n/gcd==numerator_n && denominator_x*numerator_n/gcd==denominator_n);
}

int gcd_function(int a,int b)
{
    if(b==0)
    return a;
    else
    return gcd_function(b,a%b);
}