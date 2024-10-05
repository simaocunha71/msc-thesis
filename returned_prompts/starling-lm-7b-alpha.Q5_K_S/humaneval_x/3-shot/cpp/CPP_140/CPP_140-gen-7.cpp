    int i,j;
    char chr;
    string result="";
    for (i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr==' ')
        {
        if (result.length()>0 && result[result.length()-1]=='_')
            result+='-';
        else
            result+='_';
        }
        else
            result+=chr;
    }
    return result;
}


