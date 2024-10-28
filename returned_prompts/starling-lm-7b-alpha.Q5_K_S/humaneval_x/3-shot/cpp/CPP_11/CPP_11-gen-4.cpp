    int i,length=max(a.length(),b.length());
    string result;
    for (i=0;i<length;i++)
    {
        if (i<a.length())
        {
            if (i<b.length())
            {
                result+=(a[i]==b[i])?'0':'1';
            }
            else result+='0';
        }
        else result+='0';
    }
    return result;
}



