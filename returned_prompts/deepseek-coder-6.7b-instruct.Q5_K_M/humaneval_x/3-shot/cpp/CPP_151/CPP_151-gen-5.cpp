    long long sum = 0;
    for (int i = 0; i < lst.size(); i++){
        if (lst[i] < 0 || lst[i] != int(lst[i])) continue;
        if (lst[i] % 2 == 1){
            sum += pow(lst[i], 2);
        }
    }
    return sum;
}


