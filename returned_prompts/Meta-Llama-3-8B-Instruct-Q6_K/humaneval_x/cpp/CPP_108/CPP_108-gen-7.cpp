    int count = 0;
    for(auto i : n){
        int sum = 0;
        int temp = i;
        while(temp != 0){
            sum += abs(temp % 10);
            temp /= 10;
        }
        if(sum > 0)
            count++;
    }
    return count;
}

