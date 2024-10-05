    if (x==0)
    return "0";
    else
    {
    string ret="";
    while (x>0)
    {
        ret+=(x%base)+'0';
        x=x/base;
    }
    reverse(ret.begin(), ret.end());
    return ret;
    }
}


