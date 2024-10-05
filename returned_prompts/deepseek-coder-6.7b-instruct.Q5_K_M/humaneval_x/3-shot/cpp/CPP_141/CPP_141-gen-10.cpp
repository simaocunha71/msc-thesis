    int i;
    int count = 0;
    for (i = 0; i < file_name.length(); i++){
        if (isdigit(file_name[i])){
            count++;
        }
    }
    if (count > 3)
        return "No";
    if (file_name.find('.') == string::npos)
        return "No";
    if (file_name.substr(0, file_name.find('.')).empty())
        return "No";
    if (!isalpha(file_name[0]))
        return "No";
    if (file_name.substr(file_name.find_last_of('.') + 1) != "txt" && file_name.substr(file_name.find_last_of('.') + 1) != "exe" && file_name.substr(file_name.find_last_of('.') + 1) != "dll")
        return "No";
    return "Yes";
}


