    int i;
    int numerator=0;
    int denominator=0;
    int numerator1=0;
    int denominator1=0;
    for (i=0;i<x.length();i++)
    if (x[i]=='/')
    {
        numerator=atoi(&x[0]);
        denominator=atoi(&x[i+1]);
        break;
    }
    for (i=0;i<n.length();i++)
    if (n[i]=='/')
    {
        numerator1=atoi(&n[0]);
        denominator1=atoi(&n[i+1]);
        break;
    }
    if ((numerator*denominator1)==(numerator1*denominator))
    return true;
    else
    return false;
}


