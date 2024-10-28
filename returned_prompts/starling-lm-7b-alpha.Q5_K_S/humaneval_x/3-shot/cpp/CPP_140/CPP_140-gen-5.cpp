    int i;
    string result="";
    char chr;
    for (i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr==' ')
        {
            if (result[result.length()-1]=='_')
            result+='-';
            else
            result+='_';
        }
        else
        result+=chr;
    }
    return result;
}


