    int count=0;
    int dot_count=0;
    bool valid_start=false;

    for(int i=0;i<file_name.length();i++){
        if(file_name[i]>='0' && file_name[i]<='9'){
            count++;
        }
        if(file_name[i]=='.'){
            dot_count++;
        }
        if(i==0 && (file_name[i]>='a' && file_name[i]<='z' || file_name[i]>='A' && file_name[i]<='Z')){
            valid_start=true;
        }
    }

    if(count>3 || dot_count!=1 || !valid_start || file_name.find('.')+1!=file_name.find_last_of('.'))
        return "No";
    else{
        string extension=file_name.substr(file_name.find_last_of('.')+1);
        if(extension.compare("txt") && extension.compare("exe") && extension.compare("dll"))
            return "No";
        else
            return "Yes";
    }
}

int main(){
    printf("%s\n",file_name_check("example.txt").c_str());
    printf("%s\n",file_name_check("1example.dll").c_str());
    return 0;
}
C++:

