    int count = 0;
    for(auto i: str){
        if(i == '['){
            count++;
        }
        else if(i == ']'){
            count--;
            if(count < 0){
                return false;
            }
        }
    }
    return count > 0;
}


