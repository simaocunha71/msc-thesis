    int index = -1;
    for(int i = 0; i < file_name.length(); i++) {
        if(file_name[i] == '.') {
            index = i;
            break;
        }
    }
    if(index == -1) {
        return "No";
    }
    if(file_name[0] < 'a' || file_name[0] > 'z') {
        return "No";
    }
    if(file_name[index-1] < 'a' || file_name[index-1] > 'z') {
        return "No";
    }
    if(file_name[index+1] != 't') {
        return "No";
    }
    if(file_name[index+2] != 'x') {
        return "No";
    }
    if(file_name[index+3] != 't') {
        return "No";
    }
    int cnt = 0;
    for(int i = index + 4; i < file_name.length(); i++) {
        if(file_name[i] >= '0' && file_name[i] <= '9') {
            cnt++;
        }
    }
    if(cnt > 3) {
        return "No";
    }

    return "Yes";
}

int main() {
    string file_name = "1example.dll";
    printf("%s\n", file_name_check(file_name).c_str());
}

*/












































































































































