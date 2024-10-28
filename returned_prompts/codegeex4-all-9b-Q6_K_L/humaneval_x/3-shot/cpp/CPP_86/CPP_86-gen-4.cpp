    string ans="";
    int i,j;
    for (i=0;i<s.length();i++)
    {
        string current="";
        if (s[i]==' ')
        {
            ans+=' ';
            continue;
        }
        for (j=i;j<s.length();j++)
        {
            if (s[j]==' ')
            break;
            current+=s[j];
        }
        sort(current.begin(),current.end());
        ans+=current;
        i=j;
    }
    return ans;
}

