    string s=str;
    string rev;
    int i,j;
    for (i=str.length()-1;i>=0;i--)
    {
        rev+=s[i];
    }
    for (i=str.length()-1;i>=0;i--)
    {
        if (s[i]!=rev[rev.length()-1-i])
        {
            s+=rev[rev.length()-1-i];
            break;
        }
    }
    return s;
}

