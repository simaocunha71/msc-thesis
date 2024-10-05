    string result;
    char ch;
    int i;
    for (i=0;i<s.length();i++)
    {
        ch=s[i];
        result+=ch;
        sort(result.begin()+i,result.begin()+i+1);
    }
    return result;
}



