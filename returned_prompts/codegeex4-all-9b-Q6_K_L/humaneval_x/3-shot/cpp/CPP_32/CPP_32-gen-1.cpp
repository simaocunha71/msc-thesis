    int i;
    double x=0;
    double fx=0;
    double new_x=0;
    double new_fx=0;
    double change=0.1;

    for (i=0;i<xs.size();i++)
    {
        if (xs[i]!=0)
        {
            x=i;
            fx=poly(xs,x);
            break;
        }
    }

    new_x=x+change;
    new_fx=poly(xs,new_x);
    while (abs(fx)>0.00001)
    {
        if (fx*new_fx<0)
        {
            x=new_x;
            fx=new_fx;
        }
        change=change/10;
        new_x=x+change;
        new_fx=poly(xs,new_x);
    }

    return x;
}

