    map<char, int> result;

    if(test.empty()) return result;

    string temp;
    int max_count = 0;
    for(int i=0; i<test.size(); i++){
        if(test[i] == ' '){
            if(temp.size() > 0){
                int count = 0;
                for(int j=0; j<test.size(); j++){
                    if(test[j] == temp[0]){
                        count++;
                    }
                    if(j == test.size() - 1 || test[j+1] != ' '){
                        break;
                    }
                }
                if(count > max_count){
                    max_count = count;
                    result.clear();
                    result[temp[0]] = count;
                }else if(count == max_count){
                    result[temp[0]] = count;
                }
                temp = "";
            }
        }else{
            temp += test[i];
        }
    }
    if(temp.size() > 0){
        int count = 0;
        for(int j=0; j<test.size(); j++){
            if(test[j] == temp[0]){
                count++;
            }
            if(j == test.size() - 1 || test[j+1] != ' '){
                break;
            }
        }
        if(count > max_count){
            max_count = count;
            result.clear();
            result[temp[0]] = count;
        }else if(count == max_count){
            result[temp[0]] = count;
        }
    }
    return result;
}

