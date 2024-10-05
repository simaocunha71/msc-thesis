    string res="";
    int i;
    for (i=1000000000;i>0;i/=10)
    if (x/i>=1){
        res+=change_base(x/i,base);
        x=x%i;
    }
    if (res=="")
    res+='0';

    int j;
    for (j=res.size()-1;j>=0;j--)
    {
        int dig=(res[j]-'0');
        res[j]=base+'0';
        if (dig<base)
        res[j]=dig+'0';
        else
        res[j]=dig%base+'0';
    }
    return res;
}


