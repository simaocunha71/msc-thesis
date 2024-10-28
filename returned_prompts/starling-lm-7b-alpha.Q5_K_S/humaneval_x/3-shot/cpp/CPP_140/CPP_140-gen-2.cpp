    int i,j;
    string result;
    for (i=0;i<text.length();i++)
    {
        if (text[i]!=' ')
        {
            result+=text[i];
        }
        else
        {
            if (i+1<text.length() && text[i+1]==' ')
            {
                result+="_";
                i+=1;
            }
            else
            {
                result+='-';
            }
        }
    }
    return result;
}


