    int x_numerator,x_denominator,n_numerator,n_denominator;
    int i;
    bool is_whole=true;
    for (i=0;i<x.length();i++)
    {
        if (x[i]!='/' && x[i]!='0' && x[i]!='1' && x[i]!='2' && x[i]!='3' && x[i]!='4' && x[i]!='5' && x[i]!='6' && x[i]!='7' && x[i]!='8' && x[i]!='9')
        {
            is_whole=false;
        }
    }
    for (i=0;i<n.length();i++)
    {
        if (n[i]!='/' && n[i]!='0' && n[i]!='1' && n[i]!='2' && n[i]!='3' && n[i]!='4' && n[i]!='5' && n[i]!='6' && n[i]!='7' && n[i]!='8' && n[i]!='9')
        {
            is_whole=false;
        }
    }
    x_numerator=atoi(x.substr(0,x.find('/')).c_str());
    x_denominator=atoi(x.substr(x.find('/')+1,x.length()-x.find('/')).c_str());
    n_numerator=atoi(n.substr(0,n.find('/')).c_str());
    n_denominator=atoi(n.substr(n.find('/')+1,n.length()-n.find('/')).c_str());
    int gcd_result=gcd(n_numerator*x_denominator,x_numerator*n_denominator);
    return is_whole && (n_numerator*x_denominator)/gcd_result==(x_numerator*n_denominator)/gcd_