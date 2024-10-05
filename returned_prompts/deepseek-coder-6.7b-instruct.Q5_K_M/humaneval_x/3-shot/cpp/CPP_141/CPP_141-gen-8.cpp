    int i, count = 0, dot_position;
    string valid_extensions = "txt,exe,dll";

    // Count digits and check for dot
    for (i = 0; i < file_name.size(); i++)
    {
        if (isdigit(file_name[i])) count++;
        if (file_name[i] == '.') 
        {
            dot_position = i;
            if (count > 3) return "No";
        }
    }

    // Check for no digit before dot, empty substring before dot and valid extension
    if (count == 0 && dot_position != 0 && valid_extensions.find(file_name.substr(dot_position + 1)) != string::npos) return "Yes";

    return "No";
}


