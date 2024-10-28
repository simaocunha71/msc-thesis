    string result;
    int div,i;
    for (i=0;x>0;i++)
    {
        div=x%base;
        result+=char('0'+div);
        x/=base;
    }
    reverse(result.begin(),result.end());
    return result;
}


