    int count = 0;
    for(auto ch : str){
        if(ch == '['){
            count++;
        }
        else if(ch == ']'){
            count--;
            if(count < 0){
                return false;
            }
        }
    }
    return count > 0;
}


