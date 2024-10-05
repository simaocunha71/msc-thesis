    int count=0,dot=0;
    for(int i=0;file_name[i] != '\0';i++){
        if(isdigit(file_name[i])){
            count++;
        }
        if(file_name[i] == '.'){
            dot++;
        }
    }
    if(count>3 || dot != 1){
        return "No";
    }

B:
    string valid_extension[] = {"txt", "exe", "dll"};
    string extension = file_name.substr(file_name.find_last_of(".") + 1);
    for(int i = 0; i < 3; i++){
        if(extension == valid_extension[i]){
            return "Yes";
        }
    }
    return "No";
}
int main(){
    printf("%s", file_name_check("example.txt").c_str());
    printf("%s", file_name_check("1example.dll").c_str());
    return