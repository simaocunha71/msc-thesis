    int num_of_digits=0;
    int i;
    for (i=0;i<file_name.length();i++)
    if (file_name[i]>='0' && file_name[i]<='9')
    num_of_digits+=1;
    if (num_of_digits>3)
    return "No";
    if (file_name.find(".")==string::npos)
    return "No";
    if (file_name.substr(0,file_name.find(".")).length()==0)
    return "No";
    if (file_name.substr(0,1)<'a' || file_name.substr(0,1)>'z')
    if (file_name.substr(0,1)<'A' || file_name.substr(0,1)>'Z')
    return "No";
    if (file_name.substr(file_name.find(".")+1)!="txt" && file_name.substr(file_name.find(".")+1)!="exe" && file_name.substr(file_name.find(".")+1)!="dll")
    return "No";
    return "Yes";
}



