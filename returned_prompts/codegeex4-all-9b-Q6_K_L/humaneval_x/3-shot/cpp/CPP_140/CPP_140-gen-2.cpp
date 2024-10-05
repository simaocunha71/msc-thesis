    int i;
    string result="";
    int spaces=0;
    for (i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            spaces+=1;
            if (spaces==1)
            result+='_';
            if (spaces>1)
            result+='-';
        }
        else
        {
            spaces=0;
            result+=text[i];
        }
    }
    return result;
}

