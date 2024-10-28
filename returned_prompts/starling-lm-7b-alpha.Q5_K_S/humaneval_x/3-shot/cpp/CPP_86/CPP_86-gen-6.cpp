    char chr;
    int i,j;
    string result="";
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==' ')
        result+=" ";
        else
        {
            string temp="";
            for (j=0;j<s.length();j++)
            if (s[j]==chr)
            {
                temp+=s[j];
                break;
            }
            sort(temp.begin(),temp.end());
            result+=temp;
        }
    }
    return result;
}



