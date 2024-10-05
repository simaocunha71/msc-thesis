    if(file_name.size() > 3 || file_name.size() == 0){
        return "No";
    }
    int count = 0;
    for(char c : file_name){
        if(c >= 'A' && c <= 'Z') count++;
        else if(c >= 'a' && c <= 'z') count++;
    }
    if(count != 1){
        return "No";
    }
    int pos = file_name.find(".");
    if(pos == string::npos || pos == 0 || pos == file_name.size() - 1){
        return "No";
    }
    string ext = file_name.substr(pos + 1, file_name.size() - 1);
    if(ext != "txt" && ext != "exe" && ext != "dll"){
        return "No";
    }
    return "Yes";
}
int main(){
    string file_name = "example.txt";
    printf("%s\n", file_name_check(file_name).c_str());
    return 0;
}


















































































































































































































































