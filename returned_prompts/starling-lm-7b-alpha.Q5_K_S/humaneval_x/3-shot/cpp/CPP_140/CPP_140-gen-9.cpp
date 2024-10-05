    int i,j;
    int text_size=text.length();
    for (i=0;i<text_size;i++)
    {
        if (text[i]==' ')
        {
            if (i>0 && i<text_size-1 && text[i+1]==' ')
            {
                text[i]='-';
            }
            else
                text[i]='_';
        }
    }
    return text;
}


