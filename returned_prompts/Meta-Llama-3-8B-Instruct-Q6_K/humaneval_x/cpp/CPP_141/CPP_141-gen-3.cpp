    int count = 0;
    int i = 0;
    bool is_dot = false;
    bool is_valid = true;
    while (i < file_name.length()) {
        if (file_name[i] == '.') {
            is_dot = true;
            i++;
            continue;
        }
        if (file_name[i] >= '0' && file_name[i] <= '9') {
            count++;
            if (count > 3) {
                is_valid = false;
                break;
            }
        }
        if (!is_valid) {
            break;
        }
        if (file_name[i] < 'a' || file_name[i] > 'z' && file_name[i] < 'A' || file_name[i] > 'Z') {
            is_valid = false;
            break;
        }
        i++;
    }
    if (is_dot) {
        if (i >= file_name.length() || file_name[i] != '.') {
            is_valid = false;
        }
        i++;
        if (i >= file_name.length()) {
            is_valid = false;
        }
        if (file_name.substr(i) != "txt" && file_name.substr(i) != "exe" && file_name.substr(i) != "dll") {
            is_valid = false;
        }
    } else {
        is_valid = false;
    }
    if (is_valid) {
        return "Yes";
    } else {
        return "No";
    }
}
int main() {
    string file_name = "example.txt";
    printf("%s\n", file_name_check(file_name).c_str());
    return 0;
}

