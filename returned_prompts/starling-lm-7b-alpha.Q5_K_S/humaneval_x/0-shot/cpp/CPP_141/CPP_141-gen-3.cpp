    int cnt = 0;
    for (int i = 0; i < file_name.length(); i++) {
        if (file_name[i] >= '0' && file_name[i] <= '9') {
            cnt++;
        }
    }
    if (cnt > 3) {
        return "No";
    }
    int index = -1;
    for (int i = 0; i < file_name.length(); i++) {
        if (file_name[i] == '.') {
            index = i;
            break;
        }
    }
    if (index == -1) {
        return "No";
    }
    int index1 = -1;
    for (int i = index; i < file_name.length(); i++) {
        if (file_name[i] == '.') {
            index1 = i;
            break;
        }
    }
    if (index1 - index != 4) {
        return "No";
    }
    if (file_name.length() - index1 < 4) {
        return "No";
    }
    string str = file_name.substr(index1 + 1, file_name.length() - index1);
    if (str != "txt" && str != "exe" && str != "dll") {
        return "No";
    }
    if (file_name[0] < 'a' || file_name[0] > 'z' && file_name[0] < 'A' || file_name[0] > 'Z') {
        return "No";
    }
    return "Yes";
}


int main() {
    string a;
    cin >> a;
    cout << file_name_check(a);
}




















































































