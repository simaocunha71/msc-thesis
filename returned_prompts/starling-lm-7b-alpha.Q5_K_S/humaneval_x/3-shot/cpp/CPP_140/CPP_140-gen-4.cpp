    int i;
    for (i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
        if (i>0 && text[i-1]==' ')
        text[i]='-';
        else
        text[i]='_';
        }
    }
    return text;
}



