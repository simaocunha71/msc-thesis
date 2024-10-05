    string result;
    int level;
    int i;
    for (i=0;x>0;i++)
    {
        level=x%base;
        result+=level+'0';
        x/=base;
    }
    reverse(result.begin(),result.end());
    return result;
}


