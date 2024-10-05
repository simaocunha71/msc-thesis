    int i,k=0;
    char chr;
    for (i=0;i<file_name.length();i++)
    {
        chr=file_name[i];
        if (chr>='a' && chr<='z')
        {
            k+=1;
        }
        if (chr>='A' && chr<='Z')
        {
            k+=1;
        }
        if (chr>='0' && chr<='9')
        {
            k+=1;
        }
    }
    if (k>3)
    {
        return "No";
    }
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        {
            break;
        }
    }
    if (i==file_name.length())
    {
        return "No";
    }
    if (i==0)
    {
        return "No";
    }
    if (file_name[i+1]=='.' || file_name[i+1]==' ' || file_name[i+1]=='\0')
    {
        return "No";
    }
    if (file_name[i+1]!='t' || file_name[i+2]!='x' || file_name[i+3]!='t')
    {
        return "No";
    }
    if (i+4<file_name.length())
    {
        if (file_name[i+4]!='.')
        {
            return "No";
        }
    }
    if (i+5<file_name.length())
    {
        if (file_name[i+5]!='d' || file_name[i+6]!='l' || file_name[i+7]!='l')
        {
            return "No";
        }
    }
    if (i+5==file_name.length())
    {
        return "No";
    }
    return "Yes";
}


