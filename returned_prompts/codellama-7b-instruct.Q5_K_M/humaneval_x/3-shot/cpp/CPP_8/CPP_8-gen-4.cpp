    int sum=0,prod=1;
    for (int i=0;i<numbers.size();i++){
        sum+=numbers[i];
        prod*=numbers[i];
    }
    return {sum,prod};
}


