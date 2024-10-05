    int i;
    string result="";
    while (x>0)
    {
        int d=x%base;
        string s;
        if (d<10)
        {
            s=to_string(d);
        }else{
            s=to_string(d-10);
        }
        result+=s;
        x/=base;
    }
    reverse(result.begin(),result.end());
    return result;
}




