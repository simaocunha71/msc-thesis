    string res="";
    while (x>0)
    {
        res=to_string(x%base)+res;
        x/=base;
    }
    return res;
}  // Convert decimal to any base


