    int count=0;
    int pos = file_name.find('.');
    if (pos == string::npos || pos == 0 || pos == file_name.length()-1)
        return "No";
    string before_dot = file_name.substr(0, pos);
    string after_dot = file_name.substr(pos+1);
    for (int i=0;i<before_dot.length();i++)
    {
        if (isdigit(before_dot[i]))
        {
            count++;
        }
        if (count > 3)
            return "No";
    }
    if (!isalpha(before_dot[0]))
        return "No";
    if (after_dot!="txt" && after_dot!="exe" && after_dot!="dll")
        return "No";
    return "Yes";
}

