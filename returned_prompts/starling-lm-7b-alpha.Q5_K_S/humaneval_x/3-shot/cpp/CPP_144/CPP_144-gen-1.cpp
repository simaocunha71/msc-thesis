    int x_numerator,x_denominator,n_numerator,n_denominator;
    x_numerator=atoi(x.c_str());
    x_denominator=atoi(x.c_str()+x.find('/')+1);
    n_numerator=atoi(n.c_str());
    n_denominator=atoi(n.c_str()+n.find('/')+1);

    int lcm_denominator=x_denominator*n_denominator/gcd(x_denominator,n_denominator);
    int lcm_numerator=lcm_denominator/x_denominator*x_numerator;
    if (lcm_numerator%lcm_denominator==0)
    return true;
    else
    return false;
}


