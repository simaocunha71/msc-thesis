    string result="";
    int a_len=a.length();
    int b_len=b.length();
    int len=a_len;
    if(b_len>a_len) len=b_len;
    for(int i=0;i<len;i++)
    {
        if(i>=a_len)
        {
            result+=b[i];
        }
        else if(i>=b_len)
        {
            result+=a[i];
        }
        else
        {
            if(a[i]==b[i])
            {
                result+='0';
            }
            else
            {
                result+='1';
            }
        }
    }
    return result;
}

