    vector<int> counts(2,0);
    num = abs(num);
    while(num>0){
        if((num%10)%2==0)
            counts[0]++;
        else
            counts[1]++;
        num /= 10;
    }
    return counts;
}

