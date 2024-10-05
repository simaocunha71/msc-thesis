    string result="";
    while (x>=1)
    {
        result=to_string(x%base)+result;
        x/=base;
    }
    return result;
}

