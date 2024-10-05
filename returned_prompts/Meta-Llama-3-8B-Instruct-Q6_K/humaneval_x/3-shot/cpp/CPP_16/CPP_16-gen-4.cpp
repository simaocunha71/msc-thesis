    vector<char> unique_chars;
    for(int i=0; i<str.length(); i++){
        bool found=false;
        for(int j=0; j<unique_chars.size(); j++){
            if(tolower(str[i])==tolower(unique_chars[j])){
                found=true;
                break;
            }
        }
        if(!found)
            unique_chars.push_back(str[i]);
    }
    return unique_chars.size();
} 
*/



