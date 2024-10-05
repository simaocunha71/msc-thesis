    int count = 0;
    for(int i = 0; i < str.size(); i++){
        if(str[i] == '['){
            count++;
        }
        if(str[i] == ']'){
            count--;
        }
        if(count > 1){
            return true;
        }
    }
    return false;
}


