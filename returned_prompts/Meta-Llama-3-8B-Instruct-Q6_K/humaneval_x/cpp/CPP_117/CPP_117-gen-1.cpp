    vector<string> result;
    for(int i=0;i<s.length();i++){
        string temp;
        if(s[i] != ' '){
            temp += s[i];
            for(int j=i+1;j<s.length();j++){
                if(s[j] == ' '){
                    if(temp.length() - count(temp.begin(), temp.end(), 'a') - count(temp.begin(), temp.end(), 'e') - count(temp.begin(), temp.end(), 'i') - count(temp.begin(), temp.end(), 'o') - count(temp.begin(), temp.end(), 'u') >= n){
                        result.push_back(temp);
                    }
                    break;
                }
                temp += s[j];
            }
        }
    }
    return result;
}

