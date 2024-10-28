    int i;
    int count = 0;
    int dot_pos = -1;
    string valid_ext[] = {".txt", ".exe", ".dll"};
    for(i=0; i<file_name.length(); i++){
        char c = file_name[i];
        if(isdigit(c)) count++;
        if(c == '.') dot_pos = i;
    }
    if(count > 3 || !isalpha(file_name[0]) || dot_pos == -1) return "No";
    for(string ext : valid_ext){
        if(file_name.substr(dot_pos) == ext) return "Yes";
    }
    return "No";
}

