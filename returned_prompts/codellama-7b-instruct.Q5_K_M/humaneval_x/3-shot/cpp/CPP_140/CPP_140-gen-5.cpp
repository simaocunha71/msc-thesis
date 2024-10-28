    int i;
    for (i=0;i<text.size();i++)
    if (text[i]==' ')
    text[i]='_';
    for (i=1;i<text.size()-1;i++)
    if (text[i]==' ' && text[i-1]==' ' && text[i+1]==' ')
    text[i]='-';
    return text;
}


