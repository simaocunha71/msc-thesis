    int sum=0,product=1;
    for(int i=0;i<numbers.size();i++){
        sum+=numbers[i];
        product*=numbers[i];
    }
    return {sum, product};
}


