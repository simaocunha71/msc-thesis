    int dot_index=-1;
    int count_digits=0;
    int i;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        {
            dot_index=i;
        }
        else if (isdigit(file_name[i]))
        {
            count_digits+=1;
        }
    }
    if (count_digits>3 || dot_index==-1 || dot_index==0 || !isalpha(file_name[0]) || 
    (dot_index==file_name.length()-1) || (file_name.find("txt") == string::npos && 
    file_name.find("exe") == string::npos && file_name.find("dll") == string::npos) )
    {
        return "No";
    }
    else
    {
        return "Yes";
    }
}