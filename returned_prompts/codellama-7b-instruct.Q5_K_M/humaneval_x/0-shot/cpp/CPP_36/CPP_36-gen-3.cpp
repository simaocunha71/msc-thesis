    int count = 0;
    for(int i = 2; i < n; i++){
        if(i % 11 == 0 || i % 13 == 0){
            if(i % 7 == 0) count++;
        }
    }
    return count;
}
