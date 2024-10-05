    string new_s;
    int i,j;
    for (i=0;i<s.length();i++)
    if (s[i]==' ')
    new_s+=' ';
    else
    {
        for (j=i;j<s.length();j++)
        if (s[j]!=' ')
        break;
        string current=s.substr(i,j-i);
        sort(current.begin(),current.end());
        new_s+=current;
        i=j;
    }
    return new_s;
}

