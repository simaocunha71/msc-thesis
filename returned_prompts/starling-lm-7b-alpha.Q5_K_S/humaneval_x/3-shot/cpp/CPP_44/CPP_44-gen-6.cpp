    int i;
    string num="";
    while (x>0)
    {
        int r=x%base;
        if (r<10)
        num+=to_string(r);
        else
        num+=(char)('A'+r-10);
        x/=base;
    }
    return string(num.rbegin(),num.rend());
}



