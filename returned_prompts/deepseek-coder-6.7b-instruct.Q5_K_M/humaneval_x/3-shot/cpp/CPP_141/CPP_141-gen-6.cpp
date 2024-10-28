    int dot_pos=file_name.find('.');
    int digit_count=0;
    int i;
    if(dot_pos==string::npos || dot_pos==0 || dot_pos==file_name.length()-1)
        return "No";
    for(i=0;i<file_name.length();i++){
        if(isdigit(file_name[i]))
            digit_count+=1;
    }
    if(digit_count>3)
        return "No";
    if(!isalpha(file_name[0]))
        return "No";
    string file_extension=file_name.substr(dot_pos+1);
    if(file_extension.compare("txt") && file_extension.compare("exe") && file_extension.compare("dll"))
        return "No";
    return "Yes";
}


