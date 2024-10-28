    int sum = 0;
    for(int i = 0; i < lst.size(); i++){
        lst[i] = ceil(lst[i]);
        sum += pow(lst[i], 2);
    }
    return sum;
}



