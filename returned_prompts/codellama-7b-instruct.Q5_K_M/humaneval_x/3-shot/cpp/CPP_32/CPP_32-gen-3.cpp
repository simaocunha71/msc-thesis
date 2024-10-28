    double x_0=xs[0];
    double x_1=xs[1];
    double x_2=xs[2];
    double x_3=xs[3];
    double x_4=xs[4];
    if (x_0==0)
    return 0;
    if (x_2==0)
    return 0;
    if (x_0==x_1)
    return 0;
    if (x_2==x_3)
    return 0;
    if (x_3==x_4)
    return 0;
    if (x_1==0)
    return 0;
    if (x_3==0)
    return 0;
    if (x_4==0)
    return 0;
    if (x_0==x_2)
    return 0;
    if (x_0==x_3)
    return 0;
    if (x_0==x_4)
    return 0;
    if (x_1==x_4)
    return 0;
    if (x_1==x_3)
    return 0;
    if (x_1==x_2)
    return 0;
    double x_min=0;
    double x_max=0;
    if (x_0<x_1)
    x_min=x_0;
    else 
    x_min=x_1;
    if (x_2<x_3)
    x_min=x_2;
    else 
    x_min=x_3;
    if (x_4<x_min)
    x_min=x_4;
    if (x_0>x_1)
    x_max=x_0;
    else 
    x_max=x_1;
    if (x_2>x_3)
    x_max=x_2;
    else 
    x_max=x_3;
    if (x_4>x_max)
    x_max=x_4;
    double x_mid=0;
