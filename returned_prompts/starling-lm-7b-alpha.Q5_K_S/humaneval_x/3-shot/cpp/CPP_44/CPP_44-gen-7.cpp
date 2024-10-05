    string result;
    int temp;
    while (x>0)
    {
        temp=x%base;
        if (temp<10)
        result+=(temp+'0');
        else
        result+=((temp-10)+'A');
        x/=base;
    }
    reverse(result.begin(),result.end());
    return result;
}



