    int max_len=0;
    string longest_str;
    int i;
    for (i=0;i<strings.size();i++){
        if (strings[i].length()>max_len){
            max_len=strings[i].length();
            longest_str=strings[i];
        }
    }
    return longest_str;
}


