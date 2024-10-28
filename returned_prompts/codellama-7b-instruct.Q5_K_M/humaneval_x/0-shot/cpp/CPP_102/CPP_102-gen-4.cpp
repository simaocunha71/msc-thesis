    int i = 0;
    while(i <= y){
        if(i % 2 == 0 && i >= x){
            return i;
        }
        i++;
    }
    return -1;
}

