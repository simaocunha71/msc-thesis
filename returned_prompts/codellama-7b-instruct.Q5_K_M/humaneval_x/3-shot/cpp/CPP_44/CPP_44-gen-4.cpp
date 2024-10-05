    string res;
    string s;
    if (x==0)
    return "0";
    while (x>0){
        s=char(x%base+'0');
        res=s+res;
        x=x/base;
    }
    return res;
}



