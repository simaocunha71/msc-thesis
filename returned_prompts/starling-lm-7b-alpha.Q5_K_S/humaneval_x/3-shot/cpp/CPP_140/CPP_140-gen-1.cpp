    string result="";
    char chr;
    int i;
    for (i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr==' ')
        {
        if (text[i-1]=='_' && text[i+1]=='_')
        result+='-';
        else result+='_';
        }
        else result+=chr;
    }
    return result;
}


