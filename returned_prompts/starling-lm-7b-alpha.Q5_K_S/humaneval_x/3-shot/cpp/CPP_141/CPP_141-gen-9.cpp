    int i,j;
    char chr;
    int count=0;
    for (i=0;i<file_name.length();i++)
    {
        chr=file_name[i];
        if ((chr>='a' && chr<='z') || (chr>='A' && chr<='Z'))
        {
            count+=1;
        }
        if (chr>='0' && chr<='9')
        {
            count+=1;
        }
    }
    if (count>3)
    {
        return "No";
    }
    int dot_loc;
    for (i=0;i<file_name.length();i++)
    {
        chr=file_name[i];
        if (chr=='.')
        {
            dot_loc=i;
            break;
        }
    }
    if (dot_loc==0)
    {
        return "No";
    }
    string postfix=".txt"+"."+"exe"+"."+"dll";
    for (i=dot_loc+1;i<file_name.length();i++)
    {
        chr=file_name[i];
        if (postfix.find(chr)==-1)
        {
            return "No";
        }
    }
    return "Yes";
}



