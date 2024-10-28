    string result="";
    int mod;
    while(x>0)
    {
        mod=x%base;
        x=x/base;
        result=to_string(mod)+result;
    }
    return result;
}


