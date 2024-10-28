    int i;
    for (i=0;i<text.length();i++)
    if (text[i]==' ')
    text[i]='_';
    for (i=0;i<text.length();i++)
    if (text[i]==' ' && text[i+1]==' ')
    text[i]='-';
    return text;
}


