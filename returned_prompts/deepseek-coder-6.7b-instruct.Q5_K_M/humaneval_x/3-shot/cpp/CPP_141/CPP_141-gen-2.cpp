    int count=0, i;
    for(i=0; i<file_name.length(); i++){
        if(isdigit(file_name[i])) count++;
    }
    if(count>3) return "No";
    
    int dot_pos = file_name.find('.');
    if(dot_pos == string::npos) return "No";
    if(dot_pos == 0 || dot_pos+1 == file_name.length()) return "No";
    if(!isalpha(file_name[0])) return "No";

    string extension = file_name.substr(dot_pos+1);
    if(extension != "txt" && extension != "exe" && extension != "dll") return "No";

    return "Yes";
}


