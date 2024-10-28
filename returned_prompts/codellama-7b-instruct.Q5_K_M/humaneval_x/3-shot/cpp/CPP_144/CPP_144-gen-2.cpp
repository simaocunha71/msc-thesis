    int x_num,x_den,n_num,n_den;
    int x_gcd;
    x_num=stoi(x.substr(0,x.find('/')));
    x_den=stoi(x.substr(x.find('/')+1));
    n_num=stoi(n.substr(0,n.find('/')));
    n_den=stoi(n.substr(n.find('/')+1));
    x_gcd=__gcd(x_num,x_den);
    n_gcd=__gcd(n_num,n_den);
    x_num/=x_gcd;
    x_den/=x_gcd;
    n_num/=n_gcd;
    n_den/=n_gcd;
    if (x_num*n_den==n_num*x_den)
    return true;
    else
    return false;
}




