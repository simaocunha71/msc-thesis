    int i,length=max(a.length(),b.length());
    string result="";
    for (i=0;i<length;i++)
    {
        if (i<a.length() && i<b.length())
        {
            if (a[i]==b[i])
            result+='0';
            else
            result+='1';
        }
        else
        {
            if (a.length()>b.length())
            result+=a[i];
            else
            result+=b[i];
        }
    }
    return result;
}



