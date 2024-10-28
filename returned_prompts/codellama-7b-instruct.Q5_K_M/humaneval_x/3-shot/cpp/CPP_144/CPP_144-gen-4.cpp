    int x_n,x_d,n_n,n_d;
    sscanf(x.c_str(),"%d/%d",&x_n,&x_d);
    sscanf(n.c_str(),"%d/%d",&n_n,&n_d);
    if ((x_n*n_d)%n_n==0)
    return true;
    else
    return false;
}








