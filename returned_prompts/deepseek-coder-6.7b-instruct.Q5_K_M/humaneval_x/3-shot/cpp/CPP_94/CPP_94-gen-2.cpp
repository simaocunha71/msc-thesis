    int i, j, max_prime = -1;
    for(i = 0; i < lst.size(); i++){
        for(j = 2; j * j <= lst[i]; j++){
            if(lst[i] % j == 0)
                break;
        }
        if(j * j > lst[i] && lst[i] > max_prime)
            max_prime = lst[i];
    }
    if (max_prime == -1)
        return 0;
    int sum = 0;
    while(max_prime > 0){
        sum += max_prime % 10;
        max_prime /= 10;
    }
    return sum;
}


