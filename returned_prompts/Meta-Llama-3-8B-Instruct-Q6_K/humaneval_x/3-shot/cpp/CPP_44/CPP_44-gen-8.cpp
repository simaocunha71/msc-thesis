    string res;
    while(x>0)
    {
        res=(char)(x%base+'0')+res;
        x/=base;
    }
    return res;
}