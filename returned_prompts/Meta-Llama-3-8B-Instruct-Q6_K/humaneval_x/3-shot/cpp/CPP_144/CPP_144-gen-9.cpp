    int a,b,c,d;
    sscanf(x.c_str(),"/%d/%d",&a,&b);
    sscanf(n.c_str(),"/%d/%d",&c,&d);
    return (a*c == b*d);
}