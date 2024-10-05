    int count = 0;
    for(char chr: str){
        if(chr == '[')
            count++;
        else if(chr == ']')
            count--;
        if(count < 0)
            return false;
    }
    return count > 0;
}

