    int i;
    int count=0;
    for(i=0;i<file_name.length();i++)
    {
        if(file_name[i]>='0' && file_name[i]<='9')
        count++;
    }
    if(count>3)
    return "No";
    if(file_name.find('.')==string::npos)
    return "No";
    if(!(file_name[0]>='a' && file_name[0]<='z' || file_name[0]>='A' && file_name[0]<='Z'))
    return "No";
    string extension=file_name.substr(file_name.find('.')+1);
    if(extension.compare("txt") && extension.compare("exe") && extension.compare("dll"))
    return "No";
    return "Yes";
}


