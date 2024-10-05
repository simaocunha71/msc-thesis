    string result="";
    int i;
    for (i=0;x>0;i++)
    {
        int digit=x%base;
        result+=digit+'0';
        x/=base;
    }
    reverse(result.begin(),result.end());
    return result;
}



