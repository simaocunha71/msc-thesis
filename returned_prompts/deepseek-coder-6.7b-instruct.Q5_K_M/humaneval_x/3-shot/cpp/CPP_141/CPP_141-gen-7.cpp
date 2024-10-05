    int count_digits = 0;
    int count_dots = 0;
    int i;
    for  (i=0; i<file_name.length(); i++)
    {
        if  (isdigit(file_name[i])) 
            count_digits += 1;
        if  (file_name[i] == '.') 
            count_dots += 1;
    }
    if  (count_digits > 3 || count_dots != 1 || !isalpha(file_name[0]) || (file_name.substr(file_name.find_last_of(".") + 1) != "txt" && file_name.substr(file_name.find_last_of(".") + 1) != "exe" && file_name.substr(file_name.find_last_of(".") + 1) != "dll"))
        return "No";
    return "Yes";
}


