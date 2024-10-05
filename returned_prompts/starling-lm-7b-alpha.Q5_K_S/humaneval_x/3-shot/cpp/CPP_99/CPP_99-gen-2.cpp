    int i;
    int sign=1;
    if (value[0]=='-')
    {
        sign=-1;
        i=1;
    }
    else
    {
        i=0;
    }
    float n=stof(value);
    float result=sign*round(n);
    if (i>0)
    result=-result;
    return result;
}


