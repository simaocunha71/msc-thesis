    int i,j;
    char chr;
    for (i=0;i<text.length();i++)
    {
        chr=text[i];
        if (chr==' ')
        {
            if (i==0||text[i-1]!=' ')
            text[i]='_';
            else if (i>0&&text[i-1]==' ')
            text[i]='-';
        }
    }
    return text;
}




