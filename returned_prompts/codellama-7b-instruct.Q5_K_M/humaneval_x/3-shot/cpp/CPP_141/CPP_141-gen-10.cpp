    int count_digit=0;
    string substring_before_dot,substring_after_dot;
    int index_of_dot=file_name.find(".");
    for (int i=0;i<file_name.length();i++)
    {
        if (file_name[i]>='0'&&file_name[i]<='9')
        {
            count_digit++;
        }
        if (file_name[i]=='.')
        {
            substring_before_dot=file_name.substr(0,i);
            substring_after_dot=file_name.substr(i+1,file_name.length()-i);
        }
    }
    if (count_digit>3)
        return "No";
    if (index_of_dot==-1)
        return "No";
    if (substring_before_dot.length()==0)
        return "No";
    if (substring_before_dot[0]<'a'||substring_before_dot[0]>'z'||substring_before_dot[0]<'A'||substring_before_dot[0]>'Z')
        return "No";
    if (substring_after_dot!="txt"&&substring_after_dot!="exe"&&substring_after_dot!="dll")
        return "No";
    return "Yes";
}

