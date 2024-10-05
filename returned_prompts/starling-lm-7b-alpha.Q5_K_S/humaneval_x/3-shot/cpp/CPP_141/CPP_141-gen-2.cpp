    int i,j,k;
    int digit_count=0;
    int alph_count=0;
    int ext_count=0;
    char chr;
    for (i=0;i<file_name.length();i++)
    {
        chr=file_name[i];
        if (chr=='.')
        {
        alph_count=0;
        ext_count=0;
        j=i;
        break;
        }
        if (chr>='A'&&chr<='Z')
        alph_count+=1;
        if (chr>='a'&&chr<='z')
        alph_count+=1;
        if (chr>='0'&&chr<='9')
        digit_count+=1;
    }
    if (alph_count==0||digit_count>3)
    return "No";
    if (file_name.length()==j)
    return "No";
    if (file_name[file_name.length()-1]=='.'||file_name[file_name.length()-2]=='.')
    return "No";
    for (i=j+1;i<file_name.length();i++)
    {
        chr=file_name[i];
        if (chr>='a'&&chr<='z')
        alph_count+=1;
        if (chr>='A'&&chr<='Z')
        alph_count+=1;
        if (chr>='0'&&chr<='9')
        ext_count+=1;
        if (ext_count>1)
        return "No";
    }
    if (alph_count==0)
    return "No";
    if (ext_count==0)
    return "No";
    return "Yes";
}


