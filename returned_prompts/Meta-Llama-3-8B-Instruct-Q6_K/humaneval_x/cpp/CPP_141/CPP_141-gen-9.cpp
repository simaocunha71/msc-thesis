    int count = 0;
    for(int i = 0; i < file_name.length(); i++){
        if(file_name[i] >= '0' && file_name[i] <= '9') count++;
    }
    if(count > 3) return "No";

    int pos = file_name.find('.');
    if(pos == -1) return "No";
    string before = file_name.substr(0, pos);
    string after = file_name.substr(pos+1);

    if(before.empty()) return "No";
    if(before[0] < 'a' || before[0] > 'z' && before[0] < 'A' || before[0] > 'Z') return "No";

    if(after != "txt" && after != "exe" && after != "dll") return "No";
    return "Yes";
} 
