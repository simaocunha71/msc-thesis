    // Check for more than three digits
    int count = 0;
    for (int i = 0; i < file_name.length(); i++) {
        if (isdigit(file_name[i])) {
            count++;
            if (count > 3) {
                return "No";
            }
        }
    }

    // Check for exactly one dot
    int dot_count = 0;
    for (int i = 0; i < file_name.length(); i++) {
        if (file_name[i] == '.') {
            dot_count++;
        }
    }
    if (dot_count != 1) {
        return "No";
    }

    // Check for the substring before the dot
    int dot_index = file_name.find('.');
    if (file_name.substr(0, dot_index).empty()) {
        return "No";
    }
    if (!isalpha(file_name[0])) {
        return "No";
    }

    // Check for the substring after the dot
    string extension = file_name.substr(dot_index + 1);
    if (extension != "txt" && extension != "exe" && extension != "dll") {
        return "No";
    }

    return "Yes";
}

int main() {
    printf("%s\n", file_name_check("example.txt").c_str());
    printf("%s\n", file_name_check("1example.dll").c_str());
    return 0;
}
