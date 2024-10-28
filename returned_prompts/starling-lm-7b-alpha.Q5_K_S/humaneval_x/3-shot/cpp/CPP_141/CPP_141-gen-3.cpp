    int i,j;
    int latin_count=0;
    int digits_count=0;
    int dot_index=-1;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        {
            dot_index=i;
            break;
        }
        if (file_name[i]>='a' && file_name[i]<='z')
        {
            latin_count+=1;
        }
        if (file_name[i]>='A' && file_name[i]<='Z')
        {
            latin_count+=1;
        }
        if (file_name[i]>='0' && file_name[i]<='9')
        {
            digits_count+=1;
        }
    }
    if (latin_count==0)
    {
        return "No";
    }
    if (digits_count>3)
    {
        return "No";
    }
    if (dot_index<0)
    {
        return "No";
    }
    string extension=file_name.substr(dot_index);
    if (extension!=".txt" && extension!=".exe" && extension!=".dll")
    {
        return "No";
    }
    return "Yes";
}


