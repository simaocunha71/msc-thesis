    int dot_count=0,digit_count=0;
    int i;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]=='.')
            dot_count++;
        if (isdigit(file_name[i]))
            digit_count++;
    }
    if (dot_count>1 || digit_count>3 || file_name[0]<'a' || file_name[0]>'z' || file_name[0]<'A' || file_name[0]>'Z' || file_name.find('.')==-string::npos || 
        (file_name.find('.')!=string::npos && (file_name.find("txt")!=string::npos || file_name.find("exe")!=string::npos || file_name.find("dll")!=string::npos)))
        return "No";
    return "Yes";
}