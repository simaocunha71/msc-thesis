    int i,j,k;
    string sub_string_before_dot, sub_string_after_dot;
    bool flag_before_dot=false;
    bool flag_after_dot=false;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
        {
            flag_after_dot=true;
            sub_string_after_dot=file_name.substr(i+1);
        }
        if (file_name[i]>='0' && file_name[i]<='9')
        {
            if (flag_after_dot==true)
            {
                return "No";
            }
            else
            {
                flag_before_dot=true;
                sub_string_before_dot=file_name.substr(0,i);
            }
        }
    }
    if (flag_before_dot==false)
    {
        return "No";
    }
    if (flag_after_dot==false)
    {
        return "No";
    }
    if (sub_string_before_dot.length()>3)
    {
        return "No";
    }
    if (sub_string_after_dot!="txt" && sub_string_after_dot!="exe" && sub_string_after_dot!="dll")
    {
        return "No";
    }
    return "Yes";
}


