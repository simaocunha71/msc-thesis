    string result;
    int i,temp;
    int num_digits = log10(x)+1;
    if (shift>num_digits)
    {
        string temp = to_string(x);
        reverse(temp.begin(),temp.end());
        return temp;
    }
    for (i=0;i<num_digits-shift;i++)
    {
        result+=to_string((x%10));
        x/=10;
    }
    result+=to_string(x);
    reverse(result.begin(),result.end());
    return result;
}






