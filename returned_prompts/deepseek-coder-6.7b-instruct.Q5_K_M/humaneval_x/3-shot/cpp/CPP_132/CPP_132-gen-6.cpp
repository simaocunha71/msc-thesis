    int count = 0;
    for(auto& ch : str){
        if(ch == '['){
            count++;
        }
        else{
            if(count == 0){
                return false;
            }
            count--;
        }
    }
    return count != 0;
}

