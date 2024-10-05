    string result;
    string temp;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            result+=s[i];
            temp="";
        }
        else
        {
            temp+=s[i];
            result+=temp;
            sort(temp.begin(),temp.end());
        }
    }
    return result;
}

