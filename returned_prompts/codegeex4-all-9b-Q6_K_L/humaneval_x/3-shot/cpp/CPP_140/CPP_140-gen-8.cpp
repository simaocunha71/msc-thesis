    string result="";
    int i;
    for (i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            int j=i+1;
            if (text[j]==' ')
            {
                int k=i+2;
                if (text[k]==' ')
                {
                    result+='-';
                    while (text[j]==' ')
                    {
                    j+=1;
                    }
                    i=j-1;
                    continue;
                }
            }
            result+='_';
        }
        else
        result+=text[i];
    }
    return result;
}

