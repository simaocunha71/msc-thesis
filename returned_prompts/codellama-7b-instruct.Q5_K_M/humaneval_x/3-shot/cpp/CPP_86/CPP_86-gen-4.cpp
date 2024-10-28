    string temp;
    for (int i=0;i<s.length();i++)
    {
        temp+=s[i];
        if (s[i]==' ')
        temp+=' ';
    }
    sort(temp.begin(), temp.end());
    return temp;
}



