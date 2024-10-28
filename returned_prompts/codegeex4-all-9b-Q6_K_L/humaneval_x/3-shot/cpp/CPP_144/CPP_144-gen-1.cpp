    int x_num,x_den,n_num,n_den;
    sscanf(x.c_str(),"%d/%d",&x_num,&x_den);
    sscanf(n.c_str(),"%d/%d",&n_num,&n_den);
    int gcd = 1;
    for(int i = 1; i <= x_den && i <= x_num; i++) {
        if(x_den % i == 0 && x_num % i == 0)
            gcd = i;
    }
    return ((x_den/gcd*n_num/gcd)%x_den==0);
}