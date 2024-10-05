    string result="";
    int i=0;
    while (x>0)
    {
    int mod=x%base;
    if (mod<10)
    result+=char(mod+'0');
    else
    result+=char(mod+'A'-10);
    x/=base;
    i+=1;
    }
    for (;i>=0;i--)
    result+=result[i];

    return result;
}



