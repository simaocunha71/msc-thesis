    int i, digits = 0, dot_pos = -1;
    for(i = 0; i < file_name.size(); i++){
        if(isdigit(file_name[i])) digits++;
        if(file_name[i] == '.') dot_pos = i;
    }
    if(digits > 3 || dot_pos == -1 || !isalpha(file_name[0]) || dot_pos == 0) return "No";

    string extension = file_name.substr(dot_pos + 1);
    if(extension != "txt" && extension != "exe" && extension != "dll") return "No";

    return "Yes";
}

