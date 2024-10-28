    int count=0;
    bool has_dot=false;
    bool has_letters=false;
    string before_dot="";
    string after_dot="";
    for (int i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        {
            has_dot=true;
        }
        else if (isdigit(file_name[i]))
        {
            count++;
        }
        else if (isalpha(file_name[i]))
        {
            has_letters=true;
        }
        if (has_dot)
        {
            after_dot+=file_name[i];
        }
        else
        {
            before_dot+=file_name[i];
        }
    }
    if (count>3)
    {
        return "No";
    }
    if (!has_dot)
    {
        return "No";
    }
    if (!has_letters)
    {
        return "No";
    }
    if (after_dot!="txt" && after_dot!="exe" && after_dot!="dll")
    {
        return "No";
    }
    return "Yes";
}