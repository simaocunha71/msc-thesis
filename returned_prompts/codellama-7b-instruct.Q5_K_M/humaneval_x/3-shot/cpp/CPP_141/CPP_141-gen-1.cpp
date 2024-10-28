    if (file_name.length()>3)
    return "No";
    if (file_name.find(".")==std::string::npos)
    return "No";
    if (file_name.substr(0,file_name.find(".")).find_first_not_of("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")!=std::string::npos)
    return "No";
    if (file_name.substr(file_name.find(".")+1)!="txt" && file_name.substr(file_name.find(".")+1)!="exe" && file_name.substr(file_name.find(".")+1)!="dll")
    return "No";
    return "Yes";
}



