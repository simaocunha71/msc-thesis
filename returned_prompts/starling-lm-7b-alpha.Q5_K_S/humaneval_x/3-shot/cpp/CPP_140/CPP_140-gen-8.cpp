    int i;
    for (i=0;i<text.length();i++)
    if (text[i]==' ')
    {
        if (i+1<text.length() && text[i+1]==' ')
        {
            text[i]='-';
            text[i+1]='-';
            i+=1;
        }
        else
        text[i]='_';
    }

    return text;
}




