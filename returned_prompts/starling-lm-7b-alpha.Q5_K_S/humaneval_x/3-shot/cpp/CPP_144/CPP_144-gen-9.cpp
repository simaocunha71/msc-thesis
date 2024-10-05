    int x_numerator,x_denominator,n_numerator,n_denominator;
    int i,j,k;
    x_numerator=atoi(x.substr(0,x.find("/")).c_str());
    x_denominator=atoi(x.substr(x.find("/")+1,x.length()-x.find("/")).c_str());
    n_numerator=atoi(n.substr(0,n.find("/")).c_str());
    n_denominator=atoi(n.substr(n.find("/")+1,n.length()-n.find("/")).c_str());

    for (i=2;i<=max(x_numerator,n_numerator);i++)
    {
        while (x_numerator%i==0&&n_numerator%i==0&&x_denominator%i==0&&n_denominator%i==0)
        {
            x_numerator/=i;
            x_denominator/=i;
            n_numerator/=i;
            n_denominator/=i;
        }
    }
    if (x_numerator*x_denominator==n_numerator&&x_numerator*n_denominator==n_numerator*x_denominator)
    {
        return true;
    }
    return false;
}



