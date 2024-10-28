    string new_s;
    string temp_s;
    int i,j;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            sort(temp_s.begin(),temp_s.end());
            new_s+=temp_s;
            new_s+=s[i];
            temp_s="";
        }
        else
        temp_s+=s[i];
    }
    sort(temp_s.begin(),temp_s.end());
    new_s+=temp_s;
    return new_s;
}

