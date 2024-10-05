    bool has_digits=false,has_dot=false,has_extension=false;
    int i;
    for (i=0;i<file_name.length();i++)
    {
        if (isdigit(file_name[i]))
        {
        has_digits=true;
        }
        if (file_name[i]=='.')
        {
        has_dot=true;
        }
        if (has_dot)
        {
        if (i<file_name.length()-3 && file_name.substr(i+1,3)=="txt" || file_name.substr(i+1,3)=="exe" || file_name.substr(i+1,3)=="dll")
        {
        has_extension=true;
        }
        }
    }
    if (!has_digits && has_dot && has_extension && !has_extension)
    return "Yes";
    else
    return "No";
}