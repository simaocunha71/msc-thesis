    string res="";
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        res+=chr;
        sort(res.begin(),res.end());
        res+=' ';
    }
    return res;
}




