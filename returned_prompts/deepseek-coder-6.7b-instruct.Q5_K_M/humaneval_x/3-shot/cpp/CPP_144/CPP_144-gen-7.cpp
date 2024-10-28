    int x_num,x_den,n_num,n_den;
    sscanf(x.c_str(),"%d/%d",&x_num,&x_den);
    sscanf(n.c_str(),"%d/%d",&n_num,&n_den);
    return (x_num * n_den) % (x_den * n_num) == 0;
}


