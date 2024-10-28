    int count=0;
    int sum, digit;
    for(int i = 0; i < n.size(); i++){
        sum = 0;
        while(n[i] != 0){
            digit = n[i] % 10;
            sum += digit;
            n[i] = n[i] / 10;
        }
        if(sum > 0) count++;
    }
    return count;
}


