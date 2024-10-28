    int i;
    string ret;
    int space_count=0;
    for (i=0;i<text.length();i++)
    {
        if (text[i]==' ')
        {
            space_count+=1;
            if (space_count==2)
            ret+='-';
        }
        else
        {
            ret+=text[i];
            space_count=0;
        }
    }
    return ret;
}

