    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] % 2 == 0 && i % 2 != 0){
            sum += lst[i];
        }
    }
    return sum;
}

B:
    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        if(lst[i] % 2 == 0 && i % 2 == 0){
            sum += lst[i];
        }
    }
    return sum;

C:
    int sum = 0;
    for(int i = 1; i < lst.size(); i += 2){
        if(lst[i] % 2 == 0){
            sum += lst[i];
        }
    }
    return sum;

D:
    int sum = 0;
    for(int i = 1; i < lst.size(); i++){
        if(lst[i] % 2 == 0 && i % 2 != 0){
            sum += lst[i];
        }
    }
    return sum;
