    if (file_name[0] >= 'a' && file_name[0] <= 'z' || file_name[0] >= 'A' && file_name[0] <= 'Z') {
        for (int i = 0; i < file_name.size(); i++) {
            if (file_name[i] >= 'a' && file_name[i] <= 'z' || file_name[i] >= 'A' && file_name[i] <= 'Z') {

            } else {
                return "No";
            }
        }
    } else {
        return "No";
    }
    int count = 0;
    for (int i = 0; i < file_name.size(); i++) {
        if (file_name[i] == '.') {
            count++;
        }
    }
    if (count != 1) {
        return "No";
    }
    int count_digits = 0;
    for (int i = 0; i < file_name.size(); i++) {
        if (file_name[i] >= '0' && file_name[i] <= '9') {
            count_digits++;
        }
    }
    if (count_digits > 3) {
        return "No";
    }
    if (file_name.size() == count_digits + 1) {
        return "No";
    }
    if (file_name[file_name.size() - 1] != '.' && file_name[file_name.size() - 2] != '.') {
        return "No";
    }
    string str = file_name.substr(file_name.size() - 4, 4);
    if (str == "txt" || str == "dll" || str == "exe") {
        return "Yes";
    } else {
        return "No";
    }

}
















































