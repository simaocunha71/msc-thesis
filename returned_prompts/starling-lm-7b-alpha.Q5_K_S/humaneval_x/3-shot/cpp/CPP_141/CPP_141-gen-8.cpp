    int i,digits=0;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]>='0' && file_name[i]<='9')
        {
            digits+=1;
        }
        if (digits>3)
        {
            return "No";
        }
    }
    char chr;
    chr=file_name[0];
    if (chr<='z' && chr>='a')
    {
    }
    else
    {
        return "No";
    }
    char last_chr=file_name[file_name.length()-1];
    if (last_chr=='.' && file_name.length()>2)
    {
    }
    else
    {
        return "No";
    }
    int j;
    for (j=file_name.length()-1;j>=0;j--)
    {
        if (file_name[j]=='.')
        {
            break;
        }
    }
    for (i=j+1;i<file_name.length();i++)
    {
        chr=file_name[i];
        if (chr=='t' && chr=='x' && chr=='e')
        {
        }
        else if (chr=='d' && chr=='l' && chr=='l')
        {
        }
        else if (chr=='e' && chr=='x' && chr=='e')
        {
        }
        else
        {
            return "No";
        }
    }
    return "Yes";
}


