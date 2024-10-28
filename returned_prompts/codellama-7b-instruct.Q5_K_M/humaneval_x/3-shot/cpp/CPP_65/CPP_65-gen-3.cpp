    string result;
    int digits=log10(x)+1;
    if (shift>digits)
    {
        string temp=to_string(x);
        reverse(temp.begin(),temp.end());
        return temp;
    }
    for (int i=0;i<digits-shift;i++)
    {
        result+=to_string(x%10);
        x=x/10;
    }
    result+=to_string(x);
    reverse(result.begin(),result.end());
    return result;
}


