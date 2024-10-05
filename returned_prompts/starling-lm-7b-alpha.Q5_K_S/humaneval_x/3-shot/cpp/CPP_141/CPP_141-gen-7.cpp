    int i;
    int n_digits=0;
    for (i=0;i<file_name.length();i++)
    {
        if (file_name[i]>='0'&&file_name[i]<='9')
        {
            n_digits+=1;
        }
    }
    if (n_digits>3)
    return "No";
    if (file_name.find('.')==string::npos)
    return "No";
    if (file_name.substr(0,1)==".")
    return "No";
    if (file_name.substr(file_name.length()-4,4)!=".txt"&&file_name.substr(file_name.length()-3,3)!=".exe"&&file_name.substr(file_name.length()-3,3)!=".dll")
    return "No";
    return "Yes";
}


