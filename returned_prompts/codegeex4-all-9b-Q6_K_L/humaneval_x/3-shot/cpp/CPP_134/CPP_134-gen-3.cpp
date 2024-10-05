    int i;
    int len=txt.length();
    if (txt[len-1]>=65 && txt[len-1]<=90 || txt[len-1]>=97 && txt[len-1]<=122)
    {
        for (i=0;i<len;i++)
        {
            if (txt[i]==' ')
            {
            if (txt[len-1]>=65 && txt[len-1]<=90 || txt[len-1]>=97 && txt[len-1]<=122)
            return false;
            }
        }
    }
    return true;
}

