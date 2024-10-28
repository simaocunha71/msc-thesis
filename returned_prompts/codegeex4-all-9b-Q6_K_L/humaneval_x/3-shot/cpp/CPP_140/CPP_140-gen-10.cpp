    string fixed;
    int i;
    for (i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            fixed+='_';
            while (text[i+1]==' ')
            fixed+='-';
        }
        else
            fixed+=text[i];
    }
    return fixed;
}

